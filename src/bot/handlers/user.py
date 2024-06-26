from os import getenv, remove
from os.path import join

from aiogram import F, Router
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message
from exif_data import clear_metadata, get_exif
from keyboards import greet_reply
from options import ActionEnum, VirtualEnv
from text import greet_message, photo_message
from utils import bot

user_router = Router()


class ViewOrDelete(StatesGroup):
    Action = State()


@user_router.message(Command("start"))
async def initial_message(msg: Message):
    await msg.answer(
        greet_message, parse_mode=ParseMode.MARKDOWN, reply_markup=greet_reply
    )


@user_router.message(F.photo)
async def photo(msg: Message):
    await msg.answer(photo_message, parse_mode=ParseMode.MARKDOWN)


@user_router.message(F.document)
async def doc(msg: Message, state: FSMContext):
    action = await state.get_data()

    save_file_to = join(getenv(VirtualEnv.save_file_to), msg.document.file_name)

    with open(save_file_to, "wb") as _:
        ...

    await msg.bot.download(file=msg.document.file_id, destination=save_file_to)

    if action.get("Action") != ActionEnum.Delete:
        message, coords = get_exif(save_file_to)
        lat, long = coords

        if not message:
            await msg.answer("Metadata is empty", reply_markup=greet_reply)
        else:
            await msg.answer(message, reply_markup=greet_reply)

        if lat and long:
            await bot.send_location(chat_id=msg.chat.id, latitude=lat, longitude=long)
        remove(save_file_to)

    else:
        file = clear_metadata(save_file_to, msg.document.file_name)

        await bot.send_document(
            chat_id=msg.chat.id, document=file, reply_markup=greet_reply
        )

        remove(file.path)

        await state.clear()


@user_router.callback_query(F.data == "callback_user_metadata_view")
async def metadata_view(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await state.set_state(ViewOrDelete.Action)
    await state.update_data(Action=ActionEnum.View)
    await callback.answer("")
    await callback.message.answer("Now send your document")


@user_router.callback_query(F.data == "callback_user_metadata_delete")
async def metadata_delete(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await state.set_state(ViewOrDelete.Action)
    await state.update_data(Action=ActionEnum.Delete)
    await callback.answer("")
    await callback.message.answer("Now send your document")
