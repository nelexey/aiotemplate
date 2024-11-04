from aiogram import Router

from bot.handlers import user, admin
from .other import other_router

async def register_all_handlers(main_router: Router) -> None:
    routers = (
        *admin.register_handlers(main_router),
        *user.register_handlers(main_router),
        other_router
    )

    main_router.include_routers(*routers)