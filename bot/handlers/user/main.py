from aiogram import Router, Bot
from typing import Tuple

from .commands import commands_router
# from bot.middlewares.throttling import ThrottlingMiddleware


def register_handlers(up_router: Router, **kwargs) -> Tuple[Router, ...]:
    routers = (
        commands_router,
    )

    # commands_router.message.middleware(ThrottlingMiddleware(rate_limit=10))

    return routers