from aiogram import Router
from aiogram.types import Message


other_router = Router()

@other_router.message()
async def please_use_commands(msg: Message):
    await msg.answer('I can\'t handle')
