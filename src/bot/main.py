from aiogram import Dispatcher
from handlers.user import user_router
import asyncio
import logging
from utils import bot

dp = Dispatcher()

dp.include_router(user_router)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


asyncio.run(main())
