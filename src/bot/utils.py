from aiogram import Bot
from dotenv import load_dotenv
from os import getenv
from options import VirtualEnv

load_dotenv()

bot = Bot(getenv(VirtualEnv.bot_token))
