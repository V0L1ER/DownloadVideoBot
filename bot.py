import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import commands, callback

async def main():
    load_dotenv()
    token = os.getenv('BOT_TOKEN')
    bot = Bot(token)
    dp = Dispatcher()
    try:
        if not os.path.exists("downloads"):
            os.makedirs("downloads")
        dp.include_router(commands.router)
        dp.include_router(callback.router)
        print("Bot Start")
        await dp.start_polling(bot)
        await bot.session.close()  # Закрытие сессии
    except Exception as ex:
        print(f"There is an Exception: {ex}")
        
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
