import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from handlers import router

TOKEN = "YOUR_TOKEN"
bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if name == "main":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
