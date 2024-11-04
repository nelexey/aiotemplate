from aiogram import Router
from typing import Tuple

from .commands import commands_router


def register_handlers(up_router: Router) -> Tuple[Router, ...]:
    routers = (
        commands_router,
    )

    return routers