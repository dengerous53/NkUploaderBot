import os
import datetime
from pyromod import listen
from .config import Config
from pyrogram import Client




import logging
import logging.config
from pyrogram import Client 

from aiohttp import web
from Uploader.web_support import web_server
from Uploader.config import Config
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)







import logging
from Uploader.config import Config
from pyrogram import Client, __version__
from pyrogram.raw.all import layer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)



class Bot(Client):

    def __init__(self):
        super().__init__(
            name="uploader",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(
                root="uploader/plugins"
            )
        )

    async def start(self):
        await super().start()
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, Config.PORT).start()
        LOGGER.info(f"Bot 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 ⚡️⚡️⚡️")
        

    async def stop(self, *args):
        await super().stop()
        LOGGER.info("Bot Stopped!")


if __name__ == "__main__":
    app = Bot()
    app.run()
