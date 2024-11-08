from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

from bot.keyboards.inline import create_inline_keyboard
# from bot.middlewares.throttling import ThrottlingMiddleware

commands_router = Router()

# commands_router.message.middleware(ThrottlingMiddleware(rate_limit=1))

@commands_router.message(Command('start'))
async def start_command(m: Message):
    await m.answer(f'Hello {m.chat.id}')