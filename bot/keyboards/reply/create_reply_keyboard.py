from typing import List
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def create_reply_keyboard(data: List[str], row_width: int = 3) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text=item) for item in data[i:i + row_width]
        ] for i in range(0, len(data), row_width)],
        resize_keyboard=True
    )
