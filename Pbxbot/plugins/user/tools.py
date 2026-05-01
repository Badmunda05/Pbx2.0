import base64
import datetime
import math
import os
import time

from pyrogram.types import Message

from Pbxbot.core import Limits
from Pbxbot.functions.images import create_calendar
from . import Config, HelpMenu, Symbols, Pbxbot, on_message

math_cmds = ["sin", "cos", "tan", "square", "cube", "sqroot", "factorial", "power"]


@on_message("base64enc", allow_stan=True)
async def base64enc(_, message: Message):
    if len(message.command) < 2 and not message.reply_to_message:
        return await Pbxbot.delete(message, "Give me something to encode.")

    if len(message.command) >= 2:
        text = await Pbxbot.input(message)
    else:
        text = message.reply_to_message.text or message.reply_to_message.caption

    if not text:
        return await Pbxbot.delete(message, "Give me something to encode.")

    Pbx = await Pbxbot.edit(message, "Encoding...")

    encoded = base64.b64encode(text.encode()).decode()
    await Pbx.edit(f"**𝖡𝖺𝗌𝖾64 𝖤𝗇𝖼𝗈𝖽𝖾𝖽:**\n\n`{encoded}`")


@on_message("base64dec", allow_stan=True)
async def base64dec(_, message: Message):
    if len(message.command) < 2 and not message.reply_to_message:
        return await Pbxbot.delete(message, "Give me something to decode.")

    if len(message.command) >= 2:
        text = await Pbxbot.input(message)
    else:
        text = message.reply_to_message.text or message.reply_to_message.caption

    if not text:
        return await Pbxbot.delete(message, "Give me something to decode.")

    Pbx = await Pbxbot.edit(message, "Decoding...")

    decoded = base64.b64decode(text.encode()).decode()
    await Pbx.edit(f"**𝖡𝖺𝗌𝖾64 𝖣𝖾𝖼𝗈𝖽𝖾𝖽:**\n\n`{decoded}`")


@on_message(["calculate", "calc"], allow_stan=True)
async def calculator(_, message: Message):
    if len(message.command) < 2:
        return await Pbxbot.delete(message, "Give me something to calculate.")

    query = await Pbxbot.input(message)
    Pbx = await Pbxbot.edit(message, "Calculating...")
    try:
        result = eval(query)
    except Exception:
        result = "Invalid Expression"

    await Pbx.edit(
        f"**{Symbols.bullet} 𝖤𝗑𝗉𝗋𝖾𝗌𝗌𝗂𝗈𝗇:** `{query}`\n\n**{Symbols.bullet} 𝖱𝖾𝗌𝗎𝗅𝗍,,:**\n`{result}`"
    )


@on_message("math", allow_stan=True)
async def maths(_, message: Message):
    if len(message.command) < 3:
        return await Pbxbot.delete(message, "Give me something to calculate.")

    cmd = message.command[1].lower()
    query = message.command[2].lower()

    if cmd not in math_cmds:
        return await Pbxbot.delete(
            message,
            f"**Unknown command!** \n\nAvailable Commands are: \n`{'`, `'.join(math_cmds)}`",
            20,
        )

    Pbx = await Pbxbot.edit(message, "Calculating...")

    if cmd == "sin":
        result = math.sin(int(query))
    elif cmd == "cos":
        result = math.cos(int(query))
    elif cmd == "tan":
        result = math.tan(int(query))
    elif cmd == "square":
        result = int(query) * int(query)
    elif cmd == "cube":
        result = int(query) * int(query) * int(query)
    elif cmd == "sqroot":
        result = math.sqrt(int(query))
    elif cmd == "factorial":
        result = math.factorial(int(query))
    elif cmd == "power":
        result = math.pow(int(query), 2)

    await Pbx.edit(
        f"**{Symbols.bullet} 𝖤𝗑𝗉𝗋𝖾𝗌𝗌𝗂𝗈𝗇:** `{cmd} {query}`\n\n**{Symbols.bullet} 𝖱𝖾𝗌𝗎𝗅𝗍,,:**\n`{result}`"
    )


@on_message("unpack", allow_stan=True)
async def unpack(_, message: Message):
    if not message.reply_to_message or not message.reply_to_message.document:
        return await Pbxbot.delete(message, "Reply to a file to unpack.")

    Pbx = await Pbxbot.edit(message, "Unpacking...")
    filename = await message.reply_to_message.download(Config.TEMP_DIR)

    with open(filename, "rb") as f:
        data = f.read().decode()

    try:
        await Pbx.edit(
            data[: Limits.MessageLength],
            disable_web_page_preview=True,
        )
    except Exception as e:
        await Pbxbot.error(Pbx, f"`{e}`")

    os.remove(filename)


@on_message("pack", allow_stan=True)
async def pack(_, message: Message):
    if not message.reply_to_message or not message.reply_to_message.text:
        return await Pbxbot.delete(message, "Reply to a text to pack.")

    filename = f"pack_{int(time.time())}.txt"
    if len(message.command) >= 2:
        filename = message.command[1]

    with open(filename, "w") as f:
        f.write(message.reply_to_message.text)

    await message.reply_document(
        filename,
        caption=f"**💫 Packed into {filename}**",
    )

    os.remove(filename)


@on_message("calendar", allow_stan=True)
async def getcalendar(_, message: Message):
    if len(message.command) < 2:
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
    else:
        query = await Pbxbot.input(message)
        if "/" in query:
            month, year = query.split("/")
            month = int(month)
            year = int(year)
        else:
            return await Pbxbot.delete(
                message,
                "Invalid query!\n\nExample: `calendar 1/2021`",
            )

    Pbx = await Pbxbot.edit(message, "Generating calendar...")
    image = await create_calendar(year, month)

    await Pbx.reply_photo(image, caption=f"**📅 Calendar for {month}/{year}**")
    await Pbx.delete()

    os.remove(image)


HelpMenu("tools").add(
    "base64enc",
    "<reply> or <text>",
    "Encode the text to a base64 string.",
    "base64enc Hello, World!",
).add(
    "base64dec",
    "<reply> or <text>",
    "Decode the base64 string to text.",
    "base64dec SGVsbG8sIFdvcmxkIQ==",
).add(
    "calculate",
    "<expression>",
    "Calculate the expression.",
    "calculate 69*100",
    "You can also use 'calc' as an alias.",
).add(
    "math",
    "<expression>",
    "Perform some basic math operations.",
    "math sin 90",
    f"Available Commands are: \n`{'`, `'.join(math_cmds)}`",
).add(
    "unpack",
    "<reply to a file>",
    "Unpack the file and send the text content.",
    "unpack",
).add(
    "pack",
    "<reply to a text> <filename (optional)>",
    "Pack the text into a file.",
    "pack script.js",
).add(
    "calendar",
    "<month/year (optional)>",
    "Generate a calendar image.",
    "calendar 1/2024",
    "If no query is given, current month's calendar will be generated.",
).info(
    "Basic Tools"
).done()
