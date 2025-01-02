import os
import yt_dlp
import hashlib
from aiogram.types import FSInputFile
import time

def generate_url_id(url: str) -> str:
    return hashlib.md5(url.encode()).hexdigest()

async def download_and_send_media(bot, chat_id, url, media_type):
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(id)s.%(ext)s',  
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        },
        'socket_timeout': 60  
    }

    try:
        start_time = time.time()  

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        end_time = time.time()  
        elapsed_time = end_time - start_time

        
        media_file = FSInputFile(filename)
        if media_type == "video":
            await bot.send_video(chat_id, media_file, caption=f"Вот твое видео!\nВремя загрузки: {elapsed_time:.2f} секунд.")
        else:
            await bot.send_audio(chat_id, media_file, caption=f"Вот твое аудио!\nВремя загрузки: {elapsed_time:.2f} секунд.")

        os.remove(filename)  

    except Exception as e:
        await bot.send_message(chat_id, f"❌ Случилась ошибка: {e}")
