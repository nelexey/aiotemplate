from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

commands_router = Router()

@commands_router.message(Command('start'))
async def start_command(m: Message):
    await m.answer(f'Hello {m.chat.id}')