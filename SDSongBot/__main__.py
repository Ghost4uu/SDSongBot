#DeepuzMusicalz

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SDSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SDSongBot import SDbot as app
from SDSongBot import LOGGER

pm_start_text = """
<b>🇭 🇪 🇾  [{}](tg://user?id={}) ʜᴏᴡ aгε ʏᴏᴜ!! \nYTAᴜᴅɪᴏ Cʜᴀɴɴᴇʟ Bᴏᴛ. Yᴏᴜ Cᴀɴ Dɪᴡɴʟᴏᴀᴅ Sᴏɴɢᴀ ᴀɴᴅ Mᴜsɪᴄ Fʀᴏᴍ Hᴇʀᴇ.\n\n ✨Iᴍ Aʟᴡᴀʏs Hᴇʀᴇ Fᴏʀ Yᴏᴜ.

\n😌Jᴜsᴛ Sᴇɴᴅ Mᴇ Tʜᴇ Nᴀᴍᴇ Oғ Sᴏɴɢ or Mᴜsɪᴄ Tʜᴀᴛ Yᴏᴜ Wᴀɴᴛ Tᴏ Dᴏᴡɴʟᴏᴀᴅ.\n\nFᴏʀ Exᴀᴍᴘʟᴇ  ```/song stay``` 
      
\nA Mᴜsɪᴄ Dᴏᴡɴʟᴏᴅᴇʀ Bᴏᴛ Bʏ <b>Dᴇᴇᴘᴜᴢ</b> </b>
"""

@app.on_message(filters.command("start") & filters.private, group=1)
async def start(client, message, update):

    update_channel = FORCESUB_CHANNEL 
    if update_channel: 
        try: 
            user = await bot.get_chat_member(update_channel, update.chat.id) 
            if user.status == "kicked": 
               await update.reply_text("🤭 Sorry Dude, You are B A N N E D 🤣🤣🤣") 
               return 
        except UserNotParticipant: 
            #await update.reply_text(f"Join @{update_channel} To Use Me") 
            await update.reply_text( 
                text=""" <b> 🔊 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗠𝗮𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 🤭. 
Do you want Movies? If u want Movies Join our main Channel.❤️ 
Then go to the Group and click movie button, You Will get ..!😁 
 
⚠️YOU ARE NOT SUBSCRIBED OUR CHANNEL⚠️ 
 
Join on our channel to get movies ✅ 
⬇️Channel link⬇️ </b>""", 
                reply_markup=InlineKeyboardMarkup([ 
                    [ InlineKeyboardButton(text="⚡ Join My Channel⚡️", url=f"https://t.me/{update_channel}")] 
              ]) 
            ) 
            return

    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="🦋 Cʜᴀɴɴᴇʟ 🦋", url="https://t.me/YTAudio_Channel"
                    ),
                    InlineKeyboardButton(
                        text="👀 Sᴜᴘᴘᴏʀᴛ 👀", url="https://instagram.com/_.deepuz._?utm_medium=copy_link"
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
