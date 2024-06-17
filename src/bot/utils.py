from aiogram import Bot
from dotenv import load_dotenv
from os import getenv

bot = Bot(getenv("BOT_TOKEN"))
