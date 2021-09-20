#SDBOTs <https://t.me/SDBOTs_Inifinity>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SDSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SDSongBot import SDbot as app
from SDSongBot import LOGGER

pm_start_text = """
🇭 🇪 🇾  [{}](tg://user?id={}) ʜᴏᴡ aгε ʏᴏᴜ!! 🤓Iᴍ 𝔻𝕖𝕖𝕡𝕦𝕫𝕄𝕦𝕤𝕚𝕔𝕒𝕝 Bᴏᴛ.\n 😜Cʀᴇᴀᴛᴇᴅ Fᴏʀ @YTAudio_Channel, 🇾 🇴 🇺  Cᴀɴ Dɪᴡɴʟᴏᴀᴅ Sᴏɴɢᴀ ᴀɴᴅ Mᴜsɪᴄ Fʀᴏᴍ Hᴇʀᴇ.\n ✨Iᴍ Aʟᴡᴀʏs Hᴇʀᴇ Fᴏʀ Yᴏᴜ.

😌Jᴜsᴛ Sᴇɴᴅ Mᴇ Tʜᴇ Nᴀᴍᴇ Oғ Sᴏɴɢ/Mᴜsɪᴄ Tʜᴀᴛ Yᴏᴜ Wᴀɴᴛ Tᴏ Dᴏᴡɴʟᴏᴀᴅ. Usᴇ🙄👉 ```/song ``` Tʜɪs Cᴏᴍᴍᴀɴᴅ Bᴇғᴏʀᴇ Sᴏɴɢ/Mᴜsɪᴄ Nᴀᴍᴇ.\n 😜Fᴏʀ Exᴀᴍᴘʟᴇ  ```/song stay``` 
      
A Mᴜsɪᴄ Dᴏᴡɴʟᴏᴅᴇʀ Bᴏᴛ Bʏ <b>Dᴇᴇᴘᴜᴢ</b>
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
                        text="👀Sᴜᴘᴘᴏʀᴛ👀", url="https://t.me/Darkridersslk"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply_photo(photo="https://telegra.ph/file/fe15aa4dc983df363db11.jpg", caption=pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("✅ SDSongBot is online.")
idle()
