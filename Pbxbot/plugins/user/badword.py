import asyncio
import re

from pyrogram import filters, Client
from pyrogram.errors import MessageNotModified
from pyrogram.types import Message
from . import *
from Pbxbot.core import Config, Symbols
from Pbxbot.functions.utility import BList

from . import HelpMenu, custom_handler, db, Pbxbot, on_message


bad_words = ["nigga", "nigger", "coon", "retard", "fuck", "motherfucker"]

vulgar_filter = True


def switch():
    global vulgar_filter
    vulgar_filter = not vulgar_filter
    return vulgar_filter



@on_message("badword", allow_stan=True)
async def toggle(bot: Client, message: Message):
    c = switch()
    await message.edit("`on`" if c else "`off`")
    await asyncio.sleep(3)
    await message.delete()


@custom_handler(filters.text & filters.incoming & ~Config.AUTH_USERS & ~filters.service)
async def i_am_not_allowed_to_say_this(bot: Client, message: Message):
    if vulgar_filter:
        try:
            txt = None
            if message.caption:
                txt = message.caption
            elif message.text:
                txt = message.text

            for word in bad_words:
                try:
                    txt = re.sub(word, "bruh", txt, flags=re.IGNORECASE)
                except Exception as e:
                    print(f"{e}")

            if message.caption:
                if txt != message.caption:
                    await message.edit_caption(txt)

            elif message.text:
                if txt != message.text:
                    await message.edit(txt)
        except MessageNotModified:
            return

