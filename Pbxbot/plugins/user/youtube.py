import os
import time

import requests
from pyrogram.types import Message
from yt_dlp import YoutubeDL

from Pbxbot.functions.driver import YoutubeDriver
from Pbxbot.functions.formatter import secs_to_mins
from Pbxbot.functions.tools import progress

from . import HelpMenu, Symbols, Pbxbot, on_message


@on_message("yta", allow_stan=True)
async def youtube_audio(_, message: Message):
    if len(message.command) < 2:
        return await Pbxbot.delete(
            message, "Give a valid youtube link to download audio."
        )

    query = await Pbxbot.input(message)
    Pbx = await Pbxbot.edit(message, "Checking ...")
    status, url = YoutubeDriver.check_url(query)

    if not status:
        return await Pbxbot.delete(Pbx, url)

    await Pbx.edit("🎼 __Downloading audio ...__")
    try:
        with YoutubeDL(YoutubeDriver.song_options()) as ytdl:
            yt_data = ytdl.extract_info(url, False)
            yt_file = ytdl.prepare_filename(yt_data)
            ytdl.process_info(yt_data)

        upload_text = f"**⬆️ 𝖴𝗉𝗅𝗈𝖺𝖽𝗂𝗇𝗀 𝖲𝗈𝗇𝗀 ...** \n\n**{Symbols.anchor} 𝖳𝗂𝗍𝗅𝖾:** `{yt_data['title'][:50]}`\n**{Symbols.anchor} 𝖢𝗁𝖺𝗇𝗇𝖾𝗅:** `{yt_data['channel']}`"
        await Pbx.edit(upload_text)
        response = requests.get(f"https://i.ytimg.com/vi/{yt_data['id']}/hqdefault.jpg")
        with open(f"{yt_file}.jpg", "wb") as f:
            f.write(response.content)

        await message.reply_audio(
            f"{yt_file}.mp3",
            caption=f"**🎧 𝖳𝗂𝗍𝗅𝖾:** {yt_data['title']} \n\n**👀 𝖵𝗂𝖾𝗐𝗌:** `{yt_data['view_count']}` \n**⌛ 𝖣𝗎𝗋𝖺𝗍𝗂𝗈𝗇:** `{secs_to_mins(int(yt_data['duration']))}`",
            duration=int(yt_data["duration"]),
            performer="[тнє нєℓℓвσт]",
            title=yt_data["title"],
            thumb=f"{yt_file}.jpg",
            progress=progress,
            progress_args=(
                Pbx,
                time.time(),
                upload_text,
            ),
        )
        await Pbx.delete()
    except Exception as e:
        return await Pbxbot.delete(Pbx, f"**🍀 Audio not Downloaded:** `{e}`")

    try:
        os.remove(f"{yt_file}.jpg")
        os.remove(f"{yt_file}.mp3")
    except:
        pass


@on_message("ytv", allow_stan=True)
async def ytvideo(_, message: Message):
    if len(message.command) < 2:
        return await Pbxbot.delete(
            message, "Give a valid youtube link to download video."
        )

    query = await Pbxbot.input(message)
    Pbx = await Pbxbot.edit(message, "Checking ...")
    status, url = YoutubeDriver.check_url(query)

    if not status:
        return await Pbxbot.delete(Pbx, url)

    await Pbx.edit("🎼 __Downloading video ...__")
    try:
        with YoutubeDL(YoutubeDriver.video_options()) as ytdl:
            yt_data = ytdl.extract_info(url, True)
            yt_file = yt_data["id"]

        upload_text = f"**⬆️ 𝖴𝗉𝗅𝗈𝖺𝖽𝗂𝗇𝗀 𝖲𝗈𝗇𝗀 ...** \n\n**{Symbols.anchor} 𝖳𝗂𝗍𝗅𝖾:** `{yt_data['title'][:50]}`\n**{Symbols.anchor} 𝖢𝗁𝖺𝗇𝗇𝖾𝗅:** `{yt_data['channel']}`"
        await Pbx.edit(upload_text)
        response = requests.get(f"https://i.ytimg.com/vi/{yt_data['id']}/hqdefault.jpg")
        with open(f"{yt_file}.jpg", "wb") as f:
            f.write(response.content)

        await message.reply_video(
            f"{yt_file}.mp4",
            caption=f"**🎧 𝖳𝗂𝗍𝗅𝖾:** {yt_data['title']} \n\n**👀 𝖵𝗂𝖾𝗐𝗌:** `{yt_data['view_count']}` \n**⌛ 𝖣𝗎𝗋𝖺𝗍𝗂𝗈𝗇:** `{secs_to_mins(int(yt_data['duration']))}`",
            duration=int(yt_data["duration"]),
            thumb=f"{yt_file}.jpg",
            progress=progress,
            progress_args=(
                Pbx,
                time.time(),
                upload_text,
            ),
        )
        await Pbx.delete()
    except Exception as e:
        return await Pbxbot.delete(Pbx, f"**🍀 Video not Downloaded:** `{e}`")

    try:
        os.remove(f"{yt_file}.jpg")
        os.remove(f"{yt_file}.mp4")
    except:
        pass


@on_message("ytlink", allow_stan=True)
async def ytlink(_, message: Message):
    if len(message.command) < 2:
        return await Pbxbot.delete(message, "Give something to search on youtube.")

    query = await Pbxbot.input(message)
    Pbx = await Pbxbot.edit(message, "Searching ...")

    try:
        results = YoutubeDriver(query, 7).to_dict()
    except Exception as e:
        return await Pbxbot.delete(Pbx, f"**🍀 Error:** `{e}`")

    if not results:
        return await Pbxbot.delete(Pbx, "No results found.")

    text = f"**🔎 𝖳𝗈𝗍𝖺𝗅 𝖱𝖾𝗌𝗎𝗅𝗍𝗌 𝖥𝗈𝗎𝗇𝖽:** `{len(results)}`\n\n"
    for result in results:
        text += f"    **{Symbols.anchor} 𝖳𝗂𝗍𝗅𝖾:** `{result['title'][:50]}`\n**{Symbols.anchor} 𝖢𝗁𝖺𝗇𝗇𝖾𝗅:** `{result['channel']}`\n**{Symbols.anchor} 𝖵𝗂𝖾𝗐𝗌:** `{result['views']}`\n**{Symbols.anchor} 𝖣𝗎𝗋𝖺𝗍𝗂𝗈𝗇:** `{result['duration']}`\n**{Symbols.anchor} 𝖫𝗂𝗇𝗄:** `https://youtube.com{result['url_suffix']}`\n\n"

    await Pbx.edit(text, disable_web_page_preview=True)


HelpMenu("youtube").add(
    "yta",
    "<youtube link>",
    "Download the youtube video in .mp3 format!",
    "yta https://youtu.be/xxxxxxxxxxx",
).add(
    "ytv",
    "<youtube link>",
    "Download the youtube video in .mp4 format!",
    "ytv https://youtu.be/xxxxxxxxxxx",
).add(
    "ytlink",
    "<query>",
    "Search for a video on youtube.",
    "ytlink the Pbxbot 2.0",
).info(
    "Youtube Downloader",
).done()
