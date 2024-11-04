from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

from bot.filters.is_admin import IsAdmin

commands_router = Router()

@commands_router.message(Command('start'), IsAdmin())
async def start_command(m: Message):
    await m.answer('Hello, Admin!')