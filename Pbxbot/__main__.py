from pyrogram import idle

from Pbxbot import __version__
from Pbxbot.core import (
    Config,
    GachaBotsSetup,
    TemplateSetup,
    UserSetup,
    db,
    Pbxbot,
)
from Pbxbot.functions.tools import initialize_git
from Pbxbot.functions.utility import BList, Flood, TGraph

import asyncio

async def main():
    await Pbxbot.startup()
    await db.connect()
    await UserSetup()
    await GachaBotsSetup()
    await TemplateSetup()
    await Flood.updateFromDB()
    await BList.updateBlacklists()
    await TGraph.setup()
    await initialize_git(Config.PLUGINS_REPO)
    await Pbxbot.start_message(__version__)
    await idle()

if __name__ == "__main__":
    import sys

    if sys.version_info >= (3, 7):
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(main())
        finally:
            loop.close()
    else:
        asyncio.run(main())