import random
import asyncio

from pyrogram import Client, filters
from pyrogram.enums import MessageEntityType as MET, ChatAction as CA
from pyrogram.types import Message

from . import *

RAID_STR = [
   "🥹ਬਾਰੀ ਬਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦਾ ਬੱਲਾ ਤੇਰੀ ਭੈਣ ਦਾ ਫੁੱਦਾ ਮਾਰੇ ਗਰੁੱਪ ਦਾ ਮੇਂਬਰ ਕੱਲਾ ਕੱਲਾ😭",
"😈ਬਾਰੀ ਬਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦਾ ਆਲੂ ਪਿਓ ਤੇਰਾ ਟੈਮਪੂ ਮਾਂ ਤੇਰੀ ਚਾਲੂ😈",
"🥵ਬਾਰੀ ਬਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦਾ ਫੂਸਾ ਮੇਰਾ ਡੈਡੀ ਤੇਰੀ ਬੁੰਡ ਮਾਰੇ ਮੈ ਮਾਰਾਂ ਤੇਰੀ ਭੈਣ ਦਾ ਘੁਸਾ👅",
"🥵ਵਾਰੀ ਵਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦਾ ਸ਼ੇਮਪੂ ਮਾਂ ਤੇ bhen ਤੇਰੀ ਸਿੱਰੇ ਦੀ ਟੈਕਸੀ ਤੂੰ ਤੇ ਤੇਰਾ ਪਿਓ ਪਿੰਡ ਦੇ ਮਸ਼ਹੂਰ ਟੈਮਪੂ👅",
"😈ਵਾਰੀ ਵਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦਾ ਵੱਟਾ ਮਾਂ ਤੇ ਤੇਰੀ ਭੈਣ ਦੇ ਲੁੱਲਾ ਪਾਵਾ ਤੇਰਾ ਪਿਓ ਥੱਲੋ ਦੀ ਚੁੰਗੇ ਮੇਰਾ ਟੱਟਆ👅",
"🥺ਵਾਰੀ ਵਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦਾ ਅੰਬਾ ਤੇਰੀ ਮਾਂ ਦੇ ਸ਼ੋਲ਼ੇ ਚ ਮਾਰਾਂ 90 ਗਜ ਦਾ ਟੰਬਾ😭",
"🥹ਬਾਰੀ ਬਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦਾ ਟੰਬਾ ਤੇਰੀ ਮਾਂ ਤੇ ਚੜਜੇ ਮੇਰਾ ਪਿਓ ਤੇ me ਤੇਰੀ ਬੁੰਡ ਚ ਮਾਰਾਂ ਖਮਬਾ😈",
"😭ਬਾਰੀ ਬਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦਾ ਫੇਬੂ ਤੇਰੀ ਮਾਂ ਦਾ ਫੁੱਦੜਾ ਮਾਰੇ ਸਾਡੇ ਪਿੰਡ ਵਾਲਾ ਬਿੱਕਰ ਸੇਬੂ🥵",
"👅ਬੜੀ ਬਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦੀ ਲਾਲੀ ਤੇਰੇ ਪਿਓ ਦੇ ਮਾਰਾਂ ਲੁੱਲਾ ਤੇਰੀ ਭੈਣ ਦੇ ਸ਼ੋਲ਼ੇ ਚ ਟਰਾਲ਼ੀ👅",
"🥵ਬਾਰੀ ਬਰਸੀ ਖੱਟਣ ਗਏ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦਾ ਬੈਡ ਤੇਰੀ ਮਾਂ ਤੇ ਤੇਰੇ ਪਿਓ ਦੀ ਪੱਟਾਂ ਬੁੰਡ ਤੇਰੀ ਭੈਣ ਦੇ ਫੁੜਦੇ ਚ ਸ਼ੈੱਡ😭",
"🥹ਬਾਰੀ ਬਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦੀ ਰੀਡ ਆਵਦੀ ਮਾਂ ਤੇ ਭਵਨ ਕਰ ਨੰਗੀ ਜੇ ਮੈਚ ਨੀ ਹੁੰਦੀ ਸਪੀਡ🥹",
"🥵ਕਹਿੰਦੇ ਆਰ ਟਾਂਗਾ ਪਾਰ ਟਾਂਗਾ ਵਿਚ ਟਾਂਗਾ ਦੇ ਟੋਏ ਤੇਰੀ ਭੈਣ ਦਾ ਫੁੱਦਾ ਮਾਰਾਂ ਤੇਰਾ ਪਿਓ ਕੋਲ ਖੜਾ ਕਰੇ ਓਏ ਓਏ🥹"
"👅ਕਹਿੰਦੇ ਆਰ ਟਾਂਗਾ ਪਾਰ ਟਾਂਗਾ ਵਿਚ ਟਾਂਗਾ ਦੇ ਹੁਲ ਤੇਰੀ ਮਾਂ ਦੀ ਮਾਰਾਂ ਸ਼ੋਲੀ ਤੇਰੀ ਭੈਣ ਦੇ ਫੁੜਦੇ ਚ 10 ਗਜ ਦਾ ਲੁੱਲ🥵",
"😭ਬਾਰੀ ਬਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦੀ ਤੋਰੀ ਪਿਓ ਤੇਰਾ ਸ਼ੱਕਾ ਤੇਰੀ ਮਾਂ ਦੀ ਫੁੱਦੀ ਚ ਬਹੁਤ ਵੱਡੀ ਮੋਰੀ😭",
"🥵ਬਾਰੀ ਬਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦਾ ਕੱਮ ਤੇਰਾ ਪਿਓ ਲਾਵੇ ਚੁੱਪੇ ਤੇਰੀ ਭੈਣ ਦੇ ਫੁੜਦੇ ਚ ਡਰੱਮ👅",
"ਕੱਚ ਦੀ ਗਲਾਸੀ ਵਿਚ ਬੂਟਾ ਭੰਗ ਦਾ ਇੱਕ ਵਾਰ ਦੇਦੇ ਫੇਰ ਨੀ ਮੰਗਦਾ",
"ਕੱਚ ਦੇ ਗਲਸ ਵਿਚ 🥵👅 ਤੋਤਾ ਬੋਲਦਾ 🥵👅ਤੇਰੇ ਵਰਗੇ ਦੀ ਮੈ ਤੁਰੇ ਜਾਂਦੇ 🥵👅",
"ਵਾਰ ੀ ਵਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ 🥵👅 ਖੱਟ ਕੇ ਲਿਆਂਦਾ ਪੋਲਾ 🥵👅 ਤੇਰੀ ਭੈਣ ਦੀ ਫੁੱਦੀ 🥵👅 ਤੇਰੀ ਮਾਂ ਦਾ ਪਾਟਿਆ ਸ਼ੋਲਾ 🥵👅",
"ਜੱਟ ਬੈਠਾ ਛਾਵੇ ਤੂਤ ਤੇਰੀ ਭੈਣ ਦੀ ਭੋਸੜੀ ਵਿਚ ਦੇਵਾ ਮੂਤ ",
"ਜੱਟ ਕਰਦਾ ਹੁਣ ਕੰਮ੍ਰ  ਜਾ ਸਾਲਿਆ ਆਪਣੀ ਭੈਣ ਦੀ ਭੋਸੜੀ ਦਾ ਨਾਲਾ ਜਾ ਕੇ ਬੰਨ",
"ਜੱਟ ਖੜਾ ਕੋਲ ਨਹਿਰ ਏ  ਪਹਿਲੇ ਪਹਿਰ ਚੜਿਆ ਤੇਰੀ ਭੈਣ ਤੇ ਉੱਤਰਿਆ ਚੌਥੇ ਪਹਿਰ ਏ",
"ਜੱਟ ਦੀ ਪੂਰੀ ਸਿਰੇ ਦੀ ਟੀਮ  ਤੇਰੀ ਬੁੰਡ ਚ ਪਾਉਣਾ ਸੱਤ ਫੁੱਟ ਸਰਿਆ ਦਾ ਵੀਮ",  
"ਕੇਹਂਦਾ ਬਾਰੀ ਬਰਸੀ ਖਟਨ ਗਿਆ ਖਟ ਕੇ ਲਿਆਂਦਾ ਕਲਿਪ ਫੁਦੀ ਵਿਚ ਲਨ ਵੜ ਗਿਆ ਟਟੇ ਮਾਰਨ ਸਲਿਪ",
"ਕੇਹਂਦਾ ਬਾਰੀ ਬਰਸੀ ਖਟਨ ਗਯਾ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦੀ ਸ਼ੇਨੀ ਮੇਰੀ ਭਾਵੇਂ ਲਤ ਟੁੱਟ ਜਾਏ ਪਰਤੇਰੀ ਮੰਮੀ  ਦੀ ਫੁਦੀ ਕੰਦ ਓਥੇ ਭਠਾ ਕੇ ਲੈਣੀ 👅👅",
"ਕਹਿੰਦੇ ਤਾਰਾ ਤਾਰਾ ਤੇਰੀ ਭੇਣ ਦੀ ਚਕ ਕੇ ਲਤ ਬੁੰਡ ਮਾਰਾ👅👅👅",
"ਕੇਹਂਦਾ ਗਹਾਰਾ  ਗਹਾਰਾ ਮੁੜਕੇ ਤੂੰ ਇਹ ਗਰੁੱਪ ਚ ਨਹੁ ਦਿਖਣਾ ਜਦੋਂ ਲਨ ਚਕ ਤਾਂ ਤੇਰੇ  ਸਾਰਾ",
]

que = []
def is_reply_raid(func):
    async def get_userss(c: Client, m: Message):
        if not m.from_user:
            return
        if m.from_user.id not in que:
            return
        else:
            return await func(c,m)
    return get_userss

@custom_handler(filters.all,group=-18)
@is_reply_raid
async def _(c: Client,m: Message):
    message = random.choice(RAID_STR)
    await c.send_chat_action(m.chat.id, CA.TYPING)
    await asyncio.sleep(1)
    await m.reply_text(message)
    await c.send_chat_action(m.chat.id, CA.CANCEL)

@on_message("preplyraid", allow_stan=True)
async def activate_reply_raid(c: Client,m: Message):
    global que
    if m.forward_from:
        return
    if m.reply_to_message_id:
        repl_to = m.reply_to_message.from_user
        if not repl_to:
            await m.reply_text("Rreply to and user")
            return
        u_id = repl_to.id
        username = f"@{repl_to.username}" if repl_to.username else repl_to.mention
        Pbx = await m.reply_text("Reply Raid Activating....")
        if u_id not in que:
            que.append(u_id)
            await Pbx.edit_text(f"Reply Raid has been activated on {username}")
        else:
            await Pbx.edit_text("You already have started reply raid for this user")
    else:
        try:
            user = int(m.command[1])
        except ValueError:
            user = m.command[1]
            if m.entities[1].type == MET.TEXT_MENTION:
                user = m.entities[1].user.id
        except:
            await m.reply_text("Either reply to an user or give me and user id")
        try:
            user = await c.get_users(user)
        except Exception:
            to_del = await m.reply_text("Unable to fetch user from the given entity")
            await asyncio.sleep(10)
            await m.delete(True)
            await to_del.delete(True)
            return
        Pbx = await m.reply_text("Reply Raid Activating....")
        u_id = user.id
        username = f"@{user.username}" if user.username else user.mention
        if u_id not in que:
            que.append(u_id)
            await Pbx.edit_text(f"Reply Raid has been activated on {username}")
        else:
            await Pbx.edit_text("You already have started reply raid for this user")


@on_message("dpreplyraid", allow_stan=True)
async def deactivate_reply_raid(c: Client, m: Message):
    global que
    if m.forward_from:
        return
    if m.reply_to_message:
        reply_to = m.reply_to_message.from_user
        if not reply_to:
            await m.reply_text("reply to and user")
            return
        u_id = reply_to.id
        username = f"@{reply_to.username}" if reply_to.username else reply_to.mention
        Pbx = await m.reply_text("reply Raid De-activating....")
        try:
            if u_id in que:
                que.remove(u_id)
                await Pbx.edit_text(f"reply Raid has been De-activated on {username}")
                return
            await Pbx.edit_text("You haven't started reply raid for this user")
        except Exception:
            await Pbx.edit_text("You haven't activated reply raid for this user")
            return
        
    else:
        try:
            user = int(m.command[1])
        except ValueError:
            user = m.command[1]
            if m.entities[1].type == MET.TEXT_MENTION:
                user = m.entities[1].user.id
        try:
            user = await c.get_users(user)
        except Exception:
            to_del = await m.reply_text("Unable to fetch user from the given entity")
            await asyncio.sleep(10)
            await m.delete(True)
            await to_del.delete(True)
            return
        Pbx = await m.reply_text("reply Raid De-activating....")
        u_id = user.id
        username = f"@{user.username}" if user.username else user.mention
        try:
            if u_id in que:
                que.remove(u_id)
                await Pbx.edit_text(f"Hreply Raid has been De-activated on {username}")
                return
            await Pbx.edit_text("You haven't started reply raid for this user")
        except Exception:
            await Pbx.edit_text("You haven't activated reply raid for this user")
            return

HelpMenu("pbireplyraid").add(
    "preplyraid", None, "Starts reply raid on mentioned user.",
).add(
    "dpreplyraid", None, "Stops reply raid on mentioned user."
).info(
    "Spammer Module\nMay cause floodwait!"
).done()