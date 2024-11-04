from aiogram import types
from aiogram.filters import BaseFilter

class IsAdmin(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        # return message.chat.id == # Any chat_id from set or database
        return False
