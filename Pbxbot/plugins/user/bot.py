import os
import random
import time

from pyrogram import Client
from pyrogram.types import Message

from Pbxbot import START_TIME
from Pbxbot.core import ENV
from Pbxbot.functions.formatter import readable_time
from Pbxbot.functions.images import generate_alive_image
from Pbxbot.functions.templates import alive_template, ping_template

from . import Config, HelpMenu, db, Pbxbot, on_message, bot

from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultPhoto,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)

@on_message("alive", allow_stan=True)
async def alive(client: Client, message: Message):
    Pbx = await Pbxbot.edit(message, "ʀᴜᴋᴏ ʙᴀʙʏ ☹️✨❤️")

    img = await db.get_env(ENV.alive_pic)
    if not img:
        img = "./Pbxbot/resources/images/Pbxbot_logo.png"  # Default image

    uptime = readable_time(time.time() - START_TIME)
    caption = await alive_template(message.from_user.first_name, uptime)

    try:
        result = await client.get_inline_bot_results(bot.me.username, "alive_menu")
        await client.send_inline_bot_result(
            message.chat.id,
            result.query_id,
            result.results[0].id,
            True,
        )
        return await Pbx.delete()
    except Exception as e:
        await Pbxbot.error(Pbx, str(e), 20)
        return

@bot.on_inline_query(filters.regex("alive_menu"))
async def inline_alive(client: Client, inline_query):
    img = await db.get_env(ENV.alive_pic)
    if not img:
        img = "./Pbxbot/resources/images/Pbxbot_logo.png"  # Default image

    uptime = readable_time(time.time() - START_TIME)
    caption = await alive_template(inline_query.from_user.first_name, uptime)

    buttons = [
        [
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/PBX_CHAT"),
            InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/PBX_UPDATE"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    results = [
        InlineQueryResultPhoto(
            photo_url=img,
            thumb_url=img,
            caption=caption,
            reply_markup=reply_markup,
        )
    ]

    await inline_query.answer(results, cache_time=0)

@on_message("ping", allow_stan=True)
async def ping(client: Client, message: Message):
    start_time = time.time()
    Pbx = await Pbxbot.edit(message, "`·.·★ ᴘʙx 2.0 ★·.·´")
    
    uptime = readable_time(time.time() - START_TIME)
    end_time = time.time()
    speed = end_time - start_time
    
    caption = await ping_template(round(speed, 3), uptime, message.from_user.mention)

    try:
        result = await client.get_inline_bot_results(bot.me.username, "ping_menu")
        await client.send_inline_bot_result(
            message.chat.id,
            result.query_id,
            result.results[0].id,
            True,
        )
        return await Pbx.delete()
    except Exception as e:
        await Pbxbot.error(Pbx, str(e), 20)
        return

@bot.on_inline_query(filters.regex("ping_menu"))
async def inline_ping(client: Client, inline_query):
    img = await db.get_env(ENV.ping_pic)
    if not img:
        img = "https://telegra.ph/file/14166208a7bf871cb0aca.jpg"  # Default image

    uptime = readable_time(time.time() - START_TIME)
    
    # Speed calculation ka seedha tareeka, bas inline query receive hone ka time le rahe hain
    start_time = time.time()
    speed = round(time.time() - start_time, 3)

    caption = await ping_template(speed, uptime, inline_query.from_user.mention)

    buttons = [
        [
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/PBX_CHAT"),
            InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/PBX_UPDATE"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    results = [
        InlineQueryResultPhoto(
            photo_url=img,
            thumb_url=img,
            caption=caption,
            reply_markup=reply_markup,
        )
    ]

    await inline_query.answer(results, cache_time=0)
    
@on_message("history", allow_stan=True)
async def history(client: Client, message: Message):
    if not message.reply_to_message:
        if len(message.command) < 2:
            return await Pbxbot.delete(
                message, "Either reply to an user or give me a username to get history."
            )
        try:
            user = await client.get_users(message.command[1])
        except Exception as e:
            return await Pbxbot.error(message, f"`{str(e)}`")
    else:
        user = message.reply_to_message.from_user

    Pbx = await Pbxbot.edit(message, "Processing ...")

    try:
        response = await client.ask("@SangMata_BOT", f"{user.id}", timeout=60)
    except Exception as e:
        return await Pbxbot.error(Pbx, f"`{str(e)}`")

    if "you have used up your quota for today" in response.text:
        return await Pbxbot.delete(
            Pbx,
            f"Your quota of using SangMata Bot is over. Wait till 00:00 UTC before using it again.",
        )

    try:
        await response.delete()
        await response.request.delete()
    except:
        pass

    await Pbxbot.edit(Pbx, response.text)


HelpMenu("bot").add(
    "alive",
    None,
    "Get the alive message of the bot.",
    "alive",
    "You can also customize alive message with suitable variables for it.",
).add(
    "ping",
    None,
    "Check the ping speed and uptime of bot.",
    "ping",
    "You can also customize ping message by adding a media to it.",
).add(
    "history",
    "<reply to user>/<username/id>",
    "Get the username, name history of an user.",
    "history @II_BAD_MUNDA_II",
    "This command uses SangMata Bot to get the history.",
).info(
    "Alive Menu"
).done()
    
