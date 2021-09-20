
import os
import requests
import aiohttp
import youtube_dl

from SDSongBot import SDbot as app
from pyrogram import filters, Client
from youtube_search import YoutubeSearch
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputTextMessageContent

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))

@app.on_message(filters.command('song'))
def song(client, message):

    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('<b>🔎 Fɪɴᴅɪɴɢ ᴛʜᴇ sᴏɴɢ....</b>')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)

        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "<b>🥺 Sᴏʀʀʏ ɴᴏᴛʜɪɴɢ ɪs ғᴏᴜɴᴅ.\n\nTʀʏ ᴀɴᴏᴛʜᴇʀ ᴋᴇʏᴡᴏʀᴇᴅ Oʀ ᴍᴀʏʙᴇ sᴘᴇʟʟ ɪᴛ ᴘʀᴏᴘᴇʀʟʏ 🤪.</b>"
        )
        print(str(e))
        return
    m.edit("<b>🤓 Dᴏᴡɴʟᴏᴅᴇᴅ Bʏ @YTAudio_Channel</b>")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = '** 🤪 Uᴘʟᴏᴀᴅᴇᴅ Bʏ @YTAudio_Channel **'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        s = message.reply_audio(audio_file, caption=rep, thumb=thumb_name, parse_mode='md', title=title, duration=dur)
        m.delete()
    except Exception as e:
        m.edit('<b>🙄 Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ</b>')
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
