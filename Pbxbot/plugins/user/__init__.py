from pyrogram.enums import ChatType

from Pbxbot.core.clients import Pbxbot
from Pbxbot.core.config import Config, Symbols
from Pbxbot.core.database import db
from Pbxbot.plugins.decorator import custom_handler, on_message
from Pbxbot.plugins.help import HelpMenu

handler = Config.HANDLERS[0]
bot = Pbxbot.bot

spam_chats = []

bot_only = [ChatType.BOT]
group_n_channel = [ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL]
group_only = [ChatType.GROUP, ChatType.SUPERGROUP]
private_n_bot = [ChatType.PRIVATE, ChatType.BOT]
private_only = [ChatType.PRIVATE]
