from aiogram import Router
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from text import greet_message, photo_message
from aiogram import F
from dotenv import load_dotenv
from os import getenv

user_router = Router()


@user_router.message(Command("start"))
async def initial_message(msg: Message):
    await msg.answer(greet_message, parse_mode=ParseMode.MARKDOWN)

@user_router.message(F.photo)
async def photo(msg: Message):
    print(msg)
    await msg.answer(photo_message, parse_mode=ParseMode.MARKDOWN)    

@user_router.message(F.document)
async def doc(msg: Message):
    print(msg)
    await msg.answer('doc')

    with open(f"{getenv("SAVE_TO")}\\{msg.document.file_name}", "w") as _:
        ...

    await msg.bot.download(file=msg.document.file_id, destination=f"{getenv("SAVE_TO")}\\{msg.document.file_name}")