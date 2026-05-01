import os
import re
import time

import requests
from pyrogram.types import Message
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from Pbxbot.functions.driver import Driver

from . import HelpMenu, Pbxbot, on_message


def obtain_ids(user: str):
    response = requests.get("https://www.instagram.com/" + user)
    appid = re.search(r'appId":"(\d*)', response.text)[1]
    serverid = re.search(r'server_revision":(\d*)', response.text)[1]

    return appid, serverid


@on_message("reels", allow_stan=True)
async def instagramReels(_, message: Message):
    if len(message.command) < 2:
        return await Pbxbot.delete(
            message, "Give an instagram reels link to download."
        )

    Pbx = await Pbxbot.edit(message, "Searching...")

    query = await Pbxbot.input(message)
    isInstagramLink = lambda link: bool(
        (re.compile(r"^https?://(?:www\.)?instagram\.com/reel/")).match(link)
    )

    if not isInstagramLink(query):
        return await Pbxbot.error(Pbx, "Give a valid instagram reels link.")

    try:
        driver, _ = Driver.get()
        if not driver:
            return await Pbxbot.error(Pbx, _)

        driver.get(query)
        wait = WebDriverWait(driver, 10)
        element = wait.until(presence_of_element_located((By.TAG_NAME, "video")))
        reels = element.get_attribute("src")
        driver.quit()

        if reels:
            await Pbx.edit("Found the reel. **Downloading...**")

            binary = requests.get(reels).content
            fileName = f"reels_{int(time.time())}.mp4"
            with open(fileName, "wb") as file:
                file.write(binary)

            await Pbx.edit("Uploading...")
            await message.reply_video(
                fileName,
                caption=f"__💫 Downloaded Instagram Reels!__ \n\n**</> @PBX_CHAT**",
            )
            await Pbx.delete()
            os.remove(fileName)
        else:
            await Pbxbot.error(
                Pbx,
                "Unable to download the reel. Make sure the link is valid or the reel is not from a private account.",
            )
    except Exception as e:
        await Pbxbot.error(Pbx, f"**Error:** `{e}`")


@on_message("igpost", allow_stan=True)
async def instagramPost(_, message: Message):
    if len(message.command) < 2:
        return await Pbxbot.delete(message, "Give an instagram post link to download.")

    Pbx = await Pbxbot.edit(message, "Searching...")

    query = await Pbxbot.input(message)
    isInstagramLink = lambda link: bool(
        (re.compile(r"^https?://(?:www\.)?instagram\.com/p/")).match(link)
    )

    if not isInstagramLink(query):
        return await Pbxbot.error(Pbx, "Give a valid instagram post link.")

    try:
        driver, _ = Driver.get()
        if not driver:
            return await Pbxbot.error(Pbx, _)

        reels = []
        driver.get(query)
        wait = WebDriverWait(driver, 10)
        element = wait.until(presence_of_element_located((By.TAG_NAME, "video")))
        reels.append(element.get_attribute("src"))

        try:
            driver.find_element(By.XPATH, "//button[@aria-label='Next']").click()
            element = wait.until(presence_of_element_located((By.TAG_NAME, "video")))
            reels.append(element.get_attribute("src"))
        except Exception as e:
            driver.quit()
            return await Pbxbot.error(Pbx, f"`{e}`")

        driver.quit()

        if reels:
            await Pbx.edit("**Downloading...**")

            for reel in reels:
                binary = requests.get(reel).content
                fileName = f"post_{int(time.time())}.mp4"
                with open(fileName, "wb") as file:
                    file.write(binary)
                await message.reply_video(
                    fileName,
                    caption=f"__💫 Downloaded Instagram Post!__ \n\n**</> @PBX_CHAT**",
                )
                await Pbx.delete()
                os.remove(fileName)
        else:
            await Pbxbot.error(
                Pbx,
                "Unable to download the post. Make sure the link is valid or the post is not from a private account.",
            )
    except Exception as e:
        await Pbxbot.error(Pbx, f"`{e}`")


@on_message("iguser", allow_stan=True)
async def instagramUser(_, message: Message):
    if len(message.command) < 2:
        return await Pbxbot.delete(message, "Give an instagram username to fetch info.")

    BASE_URL = "https://i.instagram.com/api/v1/users/web_profile_info/"

    query = (await Pbxbot.input(message)).replace("@", "").strip()
    Pbx = await Pbxbot.edit(message, f"**Searching** `{query}` **on instagram**...")

    appid, serverid = obtain_ids(query)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) 20100101 Firefox/103.0",
        "Accept": "*/*",
        "Accept-Language": "en,en-US;q=0.3",
        "X-Instagram-AJAX": serverid,
        "X-IG-App-ID": appid,
        "X-ASBD-ID": "198337",
        "X-IG-WWW-Claim": "0",
        "Origin": "https://www.instagram.com",
        "DNT": "1",
        "Alt-Used": "i.instagram.com",
        "Connection": "keep-alive",
        "Referer": "https://www.instagram.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Sec-GPC": "1",
    }

    params = {"username": query}

    try:
        response: dict = requests.get(BASE_URL, params, headers=headers).json()

        if response["status"] != "ok":
            return await Pbxbot.error(
                Pbx,
                f"**Message:** `{response['message']}`\n**Required Login:** `{response['require_login']}`"
            )

        data = response["data"]["user"]
        about = data["biography"] if data["biography"] else "Not Available"
        followers = data["edge_followed_by"]["count"]
        following = data["edge_follow"]["count"]
        full_name = data["full_name"]
        is_private = data["is_private"]
        is_verified = data["is_verified"]
        posts = data["edge_owner_to_timeline_media"]["count"]
        username = data["username"]

        profile_pic = f"iguser_{int(time.time())}.jpg"
        with open(profile_pic, "wb") as f:
            f.write(requests.get(data["profile_pic_url_hd"]).content)

        await message.reply_photo(
            profile_pic,
            caption=(
                f"**🍀 𝖥𝗎𝗅𝗅 𝖭𝖺𝗆𝖾:** `{full_name}`\n"
                f"**👤 𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾:** [{username}](https://instagram.com/{username})\n"
                f"**👁‍🗨 𝖯𝗋𝗂𝗏𝖺𝗍𝖾:** `{is_private}`\n"
                f"**👑 𝖵𝖾𝗋𝗂𝖿𝗂𝖾𝖽:** `{is_verified}`\n"
                f"**📸 𝖯𝗈𝗌𝗍𝗌:** `{posts}`\n"
                f"**💫 𝖥𝗈𝗅𝗅𝗈𝗐𝖾𝗋𝗌:** `{followers}`\n"
                f"**🍂 𝖥𝗈𝗅𝗅𝗈𝗐𝗂𝗇𝗀:** `{following}`\n"
                f"**💬 𝖡𝗂𝗈:** `{about}`\n\n"
                "**</> @PBX_CHAT**"
            ),
        )
        await Pbx.delete()
        os.remove(profile_pic)
    except Exception as e:
        return await Pbxbot.error(Pbx, f"`{e}`")


HelpMenu("instagram").add(
    "reels",
    "<instagram reels link>",
    "Download instagram reels.",
    "reels https://www.instagram.com/reel/Cr24EiKNTL7/",
).add(
    "igpost", #Bugged: to-be-fixed : only downloads a single post
    "<instagram post link>",
    "Download instagram post.",
    "igpost https://www.instagram.com/p/C06rAjDJlJs/",
    "If the post has multiple videos, it will download all of them one by one.",
).add(
    "iguser", #Bugged
    "<instagram username>",
    "Get instagram user info.",
    "iguser therock",
).info(
    "Instagram Scrapper"
).done()
