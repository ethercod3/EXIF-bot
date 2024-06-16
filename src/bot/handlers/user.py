from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from text import greet_message

user_router = Router()


@user_router.message(Command("start"))
async def initial_message(msg: Message):
    await msg.answer(greet_message)
