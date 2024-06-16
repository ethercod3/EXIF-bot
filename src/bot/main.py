from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
from handlers.user import user_router
import asyncio
import logging

load_dotenv()

bot = Bot(getenv("BOT_TOKEN"))
dp = Dispatcher()

dp.include_router(user_router)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


asyncio.run(main())
