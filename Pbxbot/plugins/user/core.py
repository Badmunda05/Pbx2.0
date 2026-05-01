import importlib
import os
import sys
from pathlib import Path

from pyrogram import Client, filters
from pyrogram.enums import MessagesFilter, ParseMode
from pyrogram.types import InlineQueryResultPhoto
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent

from Pbxbot.core import ENV, Config, Symbols

from . import HelpMenu, bot, db, handler, Pbxbot, on_message

@on_message("help", allow_stan=True)
async def help(client: Client, message: Message):
    Pbx = await Pbxbot.edit(message, "**Processing...**")
    if len(message.command) == 1:
        try:
            result = await client.get_inline_bot_results(bot.me.username, "help_menu")
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

    plugin = await Pbxbot.input(message)
    if plugin.lower() in Config.CMD_MENU:
        try:
            await Pbxbot.edit(
                Pbx, Config.CMD_MENU[plugin.lower()], ParseMode.MARKDOWN
            )
            return
        except Exception as e:
            await Pbxbot.error(Pbx, str(e), 20)
            return

    available_plugins = f"{Symbols.bullet} **𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝗉𝗅𝗎𝗀𝗂𝗇𝗌:**\n\n"
    for i in sorted(list(Config.CMD_MENU.keys())):
        available_plugins += f"`{i}`, "
    available_plugins = available_plugins[:-2]
    available_plugins += (
        f"\n\n𝖣𝗈 `{handler}help <plugin name>` 𝗍𝗈 𝗀𝖾𝗍 𝖽𝖾𝗍𝖺𝗂𝗅𝖾𝖽 𝗂𝗇𝖿𝗈 𝗈𝖿 𝗍𝗁𝖺𝗍 𝗉𝗅𝗎𝗀𝗂𝗇."
    )
    await Pbxbot.edit(Pbx, available_plugins, ParseMode.MARKDOWN)


@on_message("repo", allow_stan=True)
async def repo(client: Client, message: Message):
    Pbx = await Pbxbot.edit(message, "**Repo...**")
    try:
        result = await client.get_inline_bot_results(bot.me.username, "repo_menu")
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
        
@bot.on_inline_query(filters.regex("repo_menu"))
async def inline_repo(client: Client, inline_query):
    buttons = [
        [
            InlineKeyboardButton("ʀᴇᴘᴏ", url="https://gitlab.com/Badhacker98/PBX_2.0/-/forks/new")
        ],
        [
            InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/PBX_UPDATE"),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/PBX_CHAT")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    results = [
        InlineQueryResultPhoto(
            id="repo",
            photo_url="https://files.catbox.moe/y3evsv.jpg",  # Image URL
            thumb_url="https://files.catbox.moe/y3evsv.jpg",  # Thumbnail
            title="Repository Information",
            description="Click to view the repository details",
            caption="📌 **Repo:**\n🔗 [Click Here](https://gitlab.com/Badhacker98/PBX_2.0/-/forks/new)",
            reply_markup=reply_markup
        )
    ]
    
    await inline_query.answer(results, cache_time=0)


@on_message("plinfo", allow_stan=True)
async def plugin_info(_, message: Message):
    plugin = await Pbxbot.input(message)
    if plugin.lower() in Config.CMD_MENU:
        try:
            await Pbxbot.edit(
                message, Config.CMD_MENU[plugin.lower()], ParseMode.MARKDOWN
            )
            return
        except Exception as e:
            await Pbxbot.error(message, str(e), 20)
            return
    await Pbxbot.error(message, f"**Invalid Plugin Name:** `{plugin}`", 20)


@on_message("cmdinfo", allow_stan=True)
async def command_info(_, message: Message):
    cmd = await Pbxbot.input(message)
    if cmd.lower() in Config.CMD_INFO:
        try:
            cmd_dict = Config.CMD_INFO[cmd.lower()]
            template = (
                f"**🍀 𝖯𝗅𝗎𝗀𝗂𝗇:** `{cmd_dict['plugin']}.py`\n\n"
                f"**{Symbols.anchor} 𝖢𝗈𝗆𝗆𝖺𝗇𝖽:** `{cmd_dict['command']}`\n"
                f"**{Symbols.anchor} 𝖣𝖾𝗌𝖼𝗋𝗂𝗉𝗍𝗂𝗈𝗇:** __{cmd_dict['description']}__\n"
                f"**{Symbols.anchor} 𝖤𝗑𝖺𝗆𝗉𝗅𝖾:** `{cmd_dict['example']}`\n"
                f"**{Symbols.anchor} 𝖭𝗈𝗍𝖾:** __{cmd_dict['note']}__\n"
            )
            await Pbxbot.edit(message, template, ParseMode.MARKDOWN)
            return
        except Exception as e:
            await Pbxbot.error(message, str(e), 20)
            return
    await Pbxbot.error(message, f"**Invalid Command Name:** `{cmd}`", 20)


@on_message("send", allow_stan=True)
async def send_plugin(client: Client, message: Message):
    if len(message.command) < 2:
        return await Pbxbot.delete(message, "Give me a plugin name to send.")

    plugin = message.command[1].lower().replace(".py", "").strip()
    if plugin not in Config.CMD_MENU:
        return await Pbxbot.delete(message, f"**Invalid Plugin Name:** `{plugin}`")

    try:
        await client.send_document(
            message.chat.id,
            f"./Pbxbot/plugins/user/{plugin}.py",
            caption=f"**🍀 𝖯𝗅𝗎𝗀𝗂𝗇:** `{plugin}.py`",
        )
        await Pbxbot.delete(message, f"**Sent:** `{plugin}.py`")
    except Exception as e:
        await Pbxbot.error(message, str(e), 20)


@on_message("install", allow_stan=True)
async def install_plugins(_, message: Message):
    if not message.reply_to_message or not message.reply_to_message.document:
        return await Pbxbot.delete(message, "Reply to a plugin to install it.")

    Pbx = await Pbxbot.edit(message, "**Installing...**")
    plugin_path = await message.reply_to_message.download("./Pbxbot/plugins/user/")

    if not plugin_path.endswith(".py"):
        os.remove(plugin_path)
        return await Pbxbot.error(Pbx, "**Invalid Plugin:** Not a python file.", 20)

    plugin = plugin_path.split("/")[-1].replace(".py", "").strip()
    if plugin in Config.CMD_MENU:
        os.remove(plugin_path)
        return await Pbxbot.error(
            Pbx, f"**Plugin Already Installed:** `{plugin}.py`", 20
        )

    if "(" in plugin:
        os.remove(plugin_path)
        return await Pbxbot.error(
            Pbx, f"**Plugin Already Installed:** `{plugin}.py`", 20
        )

    try:
        shortname = Path(plugin_path).stem.replace(".py", "")
        path = Path(f"Pbxbot/plugins/user/{shortname}.py")
        name = "Pbxbot.plugins.user." + shortname
        spec = importlib.util.spec_from_file_location(name, path)
        load = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(load)
        sys.modules["Pbxbot.plugins.user." + shortname] = load
        await Pbxbot.edit(Pbx, f"**Installed:** `{plugin}.py`")
    except Exception as e:
        await Pbxbot.error(Pbx, str(e), 20)
        os.remove(plugin_path)


@on_message("uninstall", allow_stan=True)
async def uninstall_plugins(_, message: Message):
    if len(message.command) < 2:
        return await Pbxbot.delete(message, "Give me a plugin name to uninstall.")

    plugin = message.command[1].lower().replace(".py", "").strip()
    if plugin not in Config.CMD_MENU:
        return await Pbxbot.delete(message, f"**Invalid Plugin Name:** `{plugin}`")

    try:
        os.remove(f"./Pbxbot/plugins/user/{plugin}.py")
        for i in Config.HELP_DICT[plugin]["commands"]:
            cmd = i["command"]
            for i in Pbxbot.users:
                i.remove_handler(cmd)
            del Config.CMD_INFO[cmd]
        del Config.HELP_DICT[plugin]
        del Config.CMD_MENU[plugin]
        await Pbxbot.delete(message, f"**Uninstalled:** `{plugin}.py`")
    except Exception as e:
        await Pbxbot.error(message, str(e), 20)


@on_message("installall", allow_stan=True)
async def installall(client: Client, message: Message):
    if len(message.command) < 2:
        return await Pbxbot.delete(
            message, "Give me channel username to install plugins."
        )

    try:
        chat = await client.get_chat(message.command[1])
    except Exception as e:
        return await Pbxbot.delete(message, f"**Invalid Channel Username:** `{e}`")

    Pbx = await Pbxbot.edit(message, f"**Installing plugins from {chat.title}...**")
    finalStr = f"{Symbols.check_mark} **𝖯𝗅𝗎𝗀𝗂𝗇𝗌 𝖨𝗇𝗌𝗍𝖺𝗅𝗅𝖾𝖽: {chat.title}**\n\n"
    count = 0

    async for msg in client.search_messages(chat.id, filter=MessagesFilter.DOCUMENT):
        if msg.document.file_name.endswith(".py"):
            dwl_path = await msg.download("./Pbxbot/plugins/user/")
            plugin = dwl_path.split("/")[-1].replace(".py", "").strip()
            if plugin in Config.CMD_MENU:
                os.remove(dwl_path)
                finalStr += (
                    f"   {Symbols.anchor} `{plugin}.py` - **𝖠𝗅𝗋𝖾𝖺𝖽𝗒 𝖨𝗇𝗌𝗍𝖺𝗅𝗅𝖾𝖽!**\n"
                )
                continue
            if "(" in plugin:
                os.remove(dwl_path)
                finalStr += (
                    f"   {Symbols.anchor} `{plugin}.py` - **𝖠𝗅𝗋𝖾𝖺𝖽𝗒 𝖨𝗇𝗌𝗍𝖺𝗅𝗅𝖾𝖽!**\n"
                )
                continue
            try:
                shortname = Path(dwl_path).stem.replace(".py", "")
                path = Path(f"Pbxbot/plugins/user/{shortname}.py")
                name = "Pbxbot.plugins.user." + shortname
                spec = importlib.util.spec_from_file_location(name, path)
                load = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(load)
                sys.modules["Pbxbot.plugins.user." + shortname] = load
                count += 1
                finalStr += f"   {Symbols.anchor} `{plugin}.py` - **𝖨𝗇𝗌𝗍𝖺𝗅𝗅𝖾𝖽!**\n"
            except Exception as e:
                os.remove(dwl_path)
                finalStr += (
                    f"   {Symbols.anchor} `{plugin}.py` - **𝖤𝗋𝗋𝗈𝗋 𝖨𝗇𝗌𝗍𝖺𝗅𝗅𝗂𝗇𝗀!**\n"
                )
                continue

    finalStr += f"\n**🍀 𝖳𝗈𝗍𝖺𝗅 𝖯𝗅𝗎𝗀𝗂𝗇𝗌 𝖨𝗇𝗌𝗍𝖺𝗅𝗅𝖾𝖽:** `{count}`"
    await Pbx.edit(finalStr, ParseMode.MARKDOWN, disable_web_page_preview=True)


@on_message("unload", allow_stan=True)
async def unload_plugins(_, message: Message):
    if len(message.command) < 2:
        return await Pbxbot.delete(message, "Give me a plugin name to unload.")

    plugin = message.command[1].lower().replace(".py", "").strip()
    if plugin not in Config.CMD_MENU:
        return await Pbxbot.delete(message, f"**Invalid Plugin Name:** `{plugin}`")

    unloaded = await db.get_env(ENV.unload_plugins) or ""
    unloaded = unloaded.split(" ")
    if plugin in unloaded:
        return await Pbxbot.delete(message, f"**Already Unloaded:** `{plugin}.py`")

    unloaded.append(plugin)
    await db.set_env(ENV.unload_plugins, " ".join(unloaded))
    await Pbxbot.delete(
        message, f"**Unloaded:** `{plugin}.py` \n\n__Restart the bot to see changes.__"
    )


@on_message("load", allow_stan=True)
async def load_plugins(_, message: Message):
    if len(message.command) < 2:
        return await Pbxbot.delete(message, "Give me a plugin name to load.")

    plugin = message.command[1].lower().replace(".py", "").strip()
    unloaded = await db.get_env(ENV.unload_plugins) or ""
    unloaded = unloaded.split(" ")
    if plugin not in unloaded:
        return await Pbxbot.delete(message, f"**Already Loaded:** `{plugin}.py`")

    unloaded.remove(plugin)
    await db.set_env(ENV.unload_plugins, " ".join(unloaded))
    await Pbxbot.delete(
        message, f"**Loaded:** `{plugin}.py` \n\n__Restart the bot to see changes.__"
    )


HelpMenu("help").add(
    "help",
    "<plugin name>",
    "Get the detailed help menu for that mentioned plugin or get the whole help menu instead.",
    "help alive",
).add("repo", None, "Get the repo link of the bot.", "repo").add(
    "plinfo",
    "<plugin name>",
    "Get the detailed info of the mentioned plugin.",
    "plinfo alive",
).add(
    "cmdinfo",
    "<command name>",
    "Get the detailed info of the mentioned command.",
    "cmdinfo alive",
).add(
    "send", "<plugin name>", "Send the mentioned plugin.", "send alive"
).add(
    "install",
    "<reply to plugin>",
    "Install the replied plugin.",
    None,
    "Do not install plugins from untrusted sources, they can be a malware. We're not responsible for any damage caused by them.",
).add(
    "uninstall",
    "<plugin name>",
    "Uninstall the mentioned plugin.",
    "uninstall alive",
    "This will remove all the commands of that plugin from the bot till a restart is initiated.",
).add(
    "installall",
    "<channel username>",
    "Install all the plugins from the mentioned channel.",
    "installall @PBX_CHAT",
    "Do not install plugins from untrusted sources, they can be a malware. We're not responsible for any damage caused by them.",
).add(
    "unload",
    "<plugin name>",
    "Unload the mentioned plugin.",
    "unload alive",
    "This will remove all the commands of that plugin from the bot permanently.",
).add(
    "load",
    "<plugin name>",
    "Load the mentioned plugin.",
    "load alive",
    "This will load all the commands of that plugin to the bot that was previously unloaded permanently.",
        )
