

import logging
from pyrogram import Client
from config import Config
from Config import API_HASH, API_ID, BOT_TOKEN, UPDATE_CHANNEL

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

SDbot = Client("DeepuzMucialz", bot_token=BOT_TOKEN, api_hash=API_HASH, api_id=API_ID, update_channel=UPDATE_CHANNEL)
