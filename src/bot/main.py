from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv

bot = Bot(getenv('BOT_TOKEN'))
dp = Dispatcher()

