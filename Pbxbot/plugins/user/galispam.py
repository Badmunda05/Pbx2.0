from . import *

from pyrogram import Client
from pyrogram.types import Message
from pyrogram.enums import ChatAction

from asyncio import sleep

x = True

@on_message("stopgalispam")
async def stopgspam(c: Client, m: Message):
    await c.send_chat_action(m.chat.id, ChatAction.CANCEL)
    await m.reply_text("Stopped gali spam")
    global x
    x = False


@on_message("galispam")
async def start_galispam(c: Client, m: Message):
    global x
    x = True
    xn = await m.reply_text("Startting galispam")
    await sleep(0.4)
    await xn.delete()
    await c.send_chat_action(m.chat.id,ChatAction.TYPING)
    while x == True:
        await m.delete()
        chat = m.chat.id
        await Pbxbot.send_message(chat, "TERIIIIII")
        await Pbxbot.send_message(chat, "MAAA KIIII")
        await Pbxbot.send_message(chat, "CHUTT MARUUUU")
        await Pbxbot.send_message(chat, "MADERRCHODD")
        await Pbxbot.send_message(chat, "BEHENN KEE LODEEE")
        await Pbxbot.send_message(chat, "TERIII MAAA")
        await Pbxbot.send_message(chat, "KOO AISAA CHODAAA")
        await Pbxbot.send_message(chat, "MADEERCHODD")
        await Pbxbot.send_message(chat, "KAALAAP GYII")
        await Pbxbot.send_message(chat, "TERII MAAA")
        await Pbxbot.send_message(chat, "TERAAA")
        await Pbxbot.send_message(chat, "KHANDAANN KO")
        await Pbxbot.send_message(chat, "ANDARRRR TKK")
        await Pbxbot.send_message(chat, "CHOD DALAAA")
        await Pbxbot.send_message(chat, "TERIIII")
        await Pbxbot.send_message(chat, "BEHENNN")
        await Pbxbot.send_message(chat, "ABHII MEREE")
        await Pbxbot.send_message(chat, "SEEEE")
        await Pbxbot.send_message(chat, "CHUDD RHI HAIII")
        await Pbxbot.send_message(chat, "MADERRCHODDD")
        await Pbxbot.send_message(chat, " TERIII")
        await Pbxbot.send_message(chat, "MAAA KIII")
        await Pbxbot.send_message(chat, "CHUTT MEE")
        await Pbxbot.send_message(chat, "HATHII KAA")
        await Pbxbot.send_message(chat, "LAUDAA")
        await Pbxbot.send_message(chat, "GHUSAA DIYAA")
        await Pbxbot.send_message(chat, "MADEERRCHODDD")
        await Pbxbot.send_message(chat, "RANDII")
        await Pbxbot.send_message(chat, "KAA")
        await Pbxbot.send_message(chat, "PILLAAA")
        await Pbxbot.send_message(chat, "BEHENCHODDD")
        await Pbxbot.send_message(chat, "TERIII")
        await Pbxbot.send_message(chat, "BEHENN")
        await Pbxbot.send_message(chat, "KIII")
        await Pbxbot.send_message(chat, "CHUTTT")
        await Pbxbot.send_message(chat, "MEEE")
        await Pbxbot.send_message(chat, "TOWERRR")
        await Pbxbot.send_message(chat, "GHUSAA DIYAA")
        await Pbxbot.send_message(chat, "MADERRRCHODD")
        await Pbxbot.send_message(chat, "TERAAA")
        await Pbxbot.send_message(chat, "BAAAP")
        await Pbxbot.send_message(chat, "HUINN")
        await Pbxbot.send_message(chat, "BSDKKKK")
        await Pbxbot.send_message(chat, "GANDD")
        await Pbxbot.send_message(chat, "MARR")
        await Pbxbot.send_message(chat, "MARRR")
        await Pbxbot.send_message(chat, "KEEE")
        await Pbxbot.send_message(chat, "ZINDAGIIII")
        await Pbxbot.send_message(chat, "ANDHERIII")
        await Pbxbot.send_message(chat, "KARRRR")
        await Pbxbot.send_message(chat, "DUGAAA")
        await Pbxbot.send_message(chat, "MADERRRCHODDD")
        await Pbxbot.send_message(chat, "BEHENNN")
        await Pbxbot.send_message(chat, "KEEE")
        await Pbxbot.send_message(chat, "LODEEE")
        await Pbxbot.send_message(chat, "AISAAA")
        await Pbxbot.send_message(chat, "CHODUGAAA")
        await Pbxbot.send_message(chat, "BSDKKK")
        await Pbxbot.send_message(chat, "PHIRRR")
        await Pbxbot.send_message(chat, "SEEE")
        await Pbxbot.send_message(chat, "KISIII")
        await Pbxbot.send_message(chat, "SEEE GANDD")
        await Pbxbot.send_message(chat, " MARANEE")
        await Pbxbot.send_message(chat, "KEE")
        await Pbxbot.send_message(chat, "LAYAKKK")
        await Pbxbot.send_message(chat, "NAHII BACHEGAAA")
        await Pbxbot.send_message(chat, "BAAAP")
        await Pbxbot.send_message(chat, "SEEE")
        await Pbxbot.send_message(chat, "PANGAA")
        await Pbxbot.send_message(chat, "LIYA HAIII")
        await Pbxbot.send_message(chat, "BSDKK TUUU")
        await Pbxbot.send_message(chat, "ANDARRR TAK")
        await Pbxbot.send_message(chat, "CHUDEGGAAA")
        await Pbxbot.send_message(chat, "TERIII")
        await Pbxbot.send_message(chat, "MAAAA")
        await Pbxbot.send_message(chat, "KAAA RAPEE")
        await Pbxbot.send_message(chat, "KARR DIYAA")
        await Pbxbot.send_message(chat, "MADERRCHODDD")
        await Pbxbot.send_message(chat, "BEHENCHODD")
        await Pbxbot.send_message(chat, "TERAAA")
        await Pbxbot.send_message(chat, "ASLIII")
        await Pbxbot.send_message(chat, "BAAAP MAINN")
        await Pbxbot.send_message(chat, "HI HUINNN")
        await Pbxbot.send_message(chat, "BSDKK")
        await Pbxbot.send_message(chat, "TERI MAA")
        await Pbxbot.send_message(chat, "KOO KOTHEE")
        await Pbxbot.send_message(chat, "PE CHODAA")
        await Pbxbot.send_message(chat, "THAA GHODII BANAKEE")
        await Pbxbot.send_message(chat, "JAKEEE")
        await Pbxbot.send_message(chat, "PUCHHH APNI")
        await Pbxbot.send_message(chat, "APNI")
        await Pbxbot.send_message(chat, "SAMJHAA LAWDE")
        await Pbxbot.send_message(chat, "MAAA SEE��")
        await Pbxbot.send_message(chat, "TERI ASLII")
        await Pbxbot.send_message(chat, "BAAAP")
        await Pbxbot.send_message(chat, "MAIN HI HUINN")
        await Pbxbot.send_message(chat, "MERAA NAJAYAZ�不")
        await Pbxbot.send_message(chat, "BETA HAI TUU")


HelpMenu("galispam").add(
    "galispam", None, "Start Gaali Spam!"
).add(
    "stopgalispam", None, "Gaali spam stop!"
).info(
    "Spammer Module\nMay get floodwait!"
).done()