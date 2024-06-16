from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

greet_reply = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="View image metadata", callback_data="callback_user_metadata_view"
            ),
            InlineKeyboardButton(
                text="Delete image metadata", callback_data="callback_user_metadata_delete"
            )
        ]
    ]
)