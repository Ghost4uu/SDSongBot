#SDBOTs <https://t.me/SDBOTs_Inifinity>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SDSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SDSongBot import SDbot as app
from SDSongBot import LOGGER

pm_start_text = """
🇭 🇪 🇾  [{}](tg://user?id={}) ʜᴏᴡ aгε ʏᴏᴜ!! 𝕀𝕞 𝐃𝐞𝐞𝐩𝐮𝐳𝐌𝐮𝐬𝐢𝐜𝐚𝐥 ʙᴏᴛ. ℂ𝕣𝕖𝕒𝕥𝕖𝕕 ᖴOᖇ @YTAudio_Channel, 🇾 🇴 🇺  ᑕᗩᑎ 𝔻𝕠𝕨𝕟𝕝𝕠𝕒𝕕 Sᴏɴɢᴀ ᴀɴᴅ Mᴜsɪᴄ ᖴᖇOᗰ ᕼᗴᖇᗴ. 🇮 🇲   𝐴𝑙𝑤𝑎𝑦𝑠 ʜᴇʀᴇ ᖴOᖇ 𝕐𝕠𝕦.

😉 Just send me the song name you want to download.😋
      ```/song Faded```
      
A bot by @SDBotsz 🇱🇰
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
                        text="Dev 🔥", url="https://t.me/Darkridersslk"
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
