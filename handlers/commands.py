import os

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

import keyboards.inline_kb as in_kb
import handlers.function as hf
import url_storage as storage

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply("Привет! Отправь мне ссылку на видео из Tiktok или Youtube и я помогу тебе скачать его.\n")
    
@router.message(lambda message: "tiktok.com" in message.text or "youtube.com" in message.text or "youtu.be" in message.text)
async def video_request(message: Message):
    url = message.text.strip()
    url_id = hf.generate_url_id(url)
    storage.url_storage[url_id] = url
    storage.save_url_storage(storage.url_storage)
    storage.url_storage = storage.load_url_storage()  # Оновлення словника
    await message.answer("Выберите формат загрузки:", reply_markup=await in_kb.format_btn(url_id=url_id))