#DeepuzMusicalz

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SDSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SDSongBot import SDbot as app
from SDSongBot import LOGGER
from config import UPDATE_CHANNEL

START_BUTTONS = InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(text="🦋 Cʜᴀɴɴᴇʟ 🦋", url="https://t.me/YTAudio_Channel"),
            InlineKeyboardButton(text="👀 Sᴜᴘᴘᴏʀᴛ 👀", url="https://instagram.com/_.deepuz._?utm_medium=copy_link")
            ]]
        )

@app.on_message(filters.command("start") & filters.private, group=1)
async def start(bot, update):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text("**🤭 Sorry Dude, You are B A N N E D 🤣🤣🤣**")
               return
        except UserNotParticipant:
            await update.reply_photo(
                "https://telegra.ph/file/0ce02ae8a6ade2c5237c9.jpg",
                caption="<b>Please Join My Updates Channel To Use This Bot</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="⚡️ Join Updates Channel ⚡️", url=f"t.me/{UPDATE_CHANNEL}")]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"@{UPDATE_CHANNEL}")
            return  
    reply_markup =  START_BUTTONS
    await update.reply_photo(
        "https://telegra.ph/file/98a2498c7f8220cb902aa.jpg",
        caption=f"<b>🇭 🇪 🇾  {update.from_user.first_name} ʜᴏᴡ aгε ʏᴏᴜ!! \nYTAᴜᴅɪᴏ Cʜᴀɴɴᴇʟ Bᴏᴛ. Yᴏᴜ Cᴀɴ Dɪᴡɴʟᴏᴀᴅ Sᴏɴɢᴀ ᴀɴᴅ Mᴜsɪᴄ Fʀᴏᴍ Hᴇʀᴇ.\n\n ✨Iᴍ Aʟᴡᴀʏs Hᴇʀᴇ Fᴏʀ Yᴏᴜ.\n😌Jᴜsᴛ Sᴇɴᴅ Mᴇ Tʜᴇ Nᴀᴍᴇ Oғ Sᴏɴɢ or Mᴜsɪᴄ Tʜᴀᴛ Yᴏᴜ Wᴀɴᴛ Tᴏ Dᴏᴡɴʟᴏᴀᴅ.\n\nFᴏʀ Exᴀᴍᴘʟᴇ  ```/song stay``` \nA Mᴜsɪᴄ Dᴏᴡɴʟᴏᴅᴇʀ Bᴏᴛ Bʏ <b>Dᴇᴇᴘᴜᴢ</b> </b>",
        reply_markup=reply_markup,
    )



app.start()
LOGGER.info("😌DeepuzMucialz is online.")
idle()
