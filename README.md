<h1 align="center"><b> 🕊️⃝‌ᴘʙx ❤️ᥫ᭡፝֟፝֟ 2.0</b></h1>

<p align="center"><img src="https://telegra.ph/file/fd8a6715f04182086b49e.jpg" alt="PbxBad"></p>

<h2 align="center">😈 Telegram Bot on Steroids!</h2>

<h3 align="center">
    ᴀ sᴍᴏᴏᴛʜ ☆ ғᴀsᴛ ᴛᴇʟᴇɢʀᴀᴍ ᴜsᴇʀʙᴏᴛ 
☆ ᴀᴅɴᴀᴄᴇ ғᴇᴀᴛᴜᴇʀs
</h3>

---

[![Telegram Group](https://img.shields.io/badge/Telegram-Group-white?&style=social&logo=telegram)](https://t.me/ll_THE_BAD_BOT_ll)
[![Telegram Channel](https://img.shields.io/badge/Telegram-Channel-white?&style=social&logo=telegram)](https://t.me/PBX_NETWORK)

---

## 🚀 Deploy To Render ⚠️ Deploy On EU Server

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

> **Steps:**
> 1. Fork this repo on GitHub
> 2. Click the Deploy to Render button above
> 3. Connect your forked repo
> 4. Fill in the required environment variables
> 5. Deploy! ✅

---

## 🔴 Deploy To Heroku

<p align="center">
    <a href="http://dashboard.heroku.com/new?template=https://github.com/Badmunda05/Pbx2.0">
        <img src="https://img.shields.io/badge/Pbxbot-Deploy%20To%20Heroku-black?style=for-the-badge&logo=heroku"/>
    </a>
</p>

**Steps:**
1. Fork & Star this Repo
2. Login to your [Heroku account](https://dashboard.heroku.com)
3. Click "Deploy to Heroku" button above
4. Fill in the required variables
5. Scale dynos and start the bot!

---

## 🖥️ Deploy on Linux VPS

1. **Update Packages:**
    ```bash
    sudo apt update && sudo apt upgrade -y
    ```

2. **Install required packages:**
    ```bash
    sudo apt install --no-install-recommends -y python3 python3-dev python3-pip python3-virtualenv git mediainfo nano ffmpeg unzip tmux
    ```

3. **Clone this repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_FORKED_REPO && cd YOUR_FORKED_REPO
   ```

4. **Set Config Variables:**
   ```bash
   bash setup
   ```
   Or manually:
   ```bash
   cp example.env .env && nano .env
   ```

5. **Install Requirements:**
    ```bash
    python3 -m virtualenv venv && source venv/bin/activate
    pip3 install -U -r requirements.txt
    ```

6. **Start the Bot:**
    ```bash
    tmux new-session -s PBXBOT
    python3 -m Pbxbot
    ```
    Press `Ctrl + B` then `D` to detach from tmux.

---

## ⚙️ Config Variables

| Variable | Description |
|---|---|
| **API_HASH** | Get from [my.telegram.org](https://my.telegram.org) |
| **API_ID** | Get from [my.telegram.org](https://my.telegram.org) |
| **BOT_TOKEN** | Get from [@BotFather](https://telegram.dog/BotFather) |
| **DATABASE_URL** | MongoDB URL from [mongo.db](https://account.mongodb.com/account/login) |
| **LOGGER_ID** | Chat ID of your logging channel/group |
| **OWNER_ID** | Your Telegram user ID |
| **HANDLERS** | Command triggers (default: `. ! , ?`) |

---

## 🧩 Writing Plugins

```python3
"""
A sample plugin for PbxBot.
"""
from . import on_message, Pbxbot, HelpMenu

@on_message("hii")
async def hi(_, message):
    await Pbxbot.edit(message, "Hello!")

HelpMenu("hii").add(
  "hii", None, "Says Hello!"
).done()
```

---

# License

This project is licensed under the [MIT License](LICENSE) —  
Feel free to use, modify, and share it with credit. ❤️

---

<h2 align="center">
  Made with ❤️ by <a href="https://github.com/PbxBad">🕊️⃝‌ʙᴀᴅ ❤️ᥫ᭡</a>
</h2>
