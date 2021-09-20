#DeepuzMusicalz

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SDSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SDSongBot import SDbot as app
from SDSongBot import LOGGER

pm_start_text = """
<b>🇭 🇪 🇾  [{}](tg://user?id={}) ʜᴏᴡ aгε ʏᴏᴜ!! Iᴍ <b>DᴇᴇᴘᴜᴢMᴜsɪᴄᴀʟ</b> Bᴏᴛ.\n 😜Cʀᴇᴀᴛᴇᴅ Fᴏʀ YTAᴜᴅɪᴏ Cʜᴀɴɴᴇʟ. Yᴏᴜ Cᴀɴ Dɪᴡɴʟᴏᴀᴅ Sᴏɴɢᴀ ᴀɴᴅ Mᴜsɪᴄ Fʀᴏᴍ Hᴇʀᴇ.\n\n ✨Iᴍ Aʟᴡᴀʏs Hᴇʀᴇ Fᴏʀ Yᴏᴜ.

\n😌Jᴜsᴛ Sᴇɴᴅ Mᴇ Tʜᴇ Nᴀᴍᴇ Oғ Sᴏɴɢ or Mᴜsɪᴄ Tʜᴀᴛ Yᴏᴜ Wᴀɴᴛ Tᴏ Dᴏᴡɴʟᴏᴀᴅ.\n\nFᴏʀ Exᴀᴍᴘʟᴇ  ```/song stay``` 
      
\nA Mᴜsɪᴄ Dᴏᴡɴʟᴏᴅᴇʀ Bᴏᴛ Bʏ <b>Dᴇᴇᴘᴜᴢ</b> </b>
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="🦋Dᴏᴡɴʟᴏᴀᴅ🦋", url="https://t.me/YTAudio_Channel"
                    ),
                    InlineKeyboardButton(
                        text="👀Sᴜᴘᴘᴏʀᴛ👀", url="https://instagram.com/_.deepuz._?utm_medium=copy_link"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply_photo(photo="https://telegra.ph/file/fe15aa4dc983df363db11.jpg", caption=pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("😌DeepuzMucialz is online.")
idle()
