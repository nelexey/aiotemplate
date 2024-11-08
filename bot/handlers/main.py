from aiogram import Router

from bot.handlers import user, admin
from .other import other_router
# from bot.middlewares.throttling import ThrottlingMiddleware

async def register_all_handlers(up_router: Router, **kwargs) -> None:
    routers = (
        *admin.register_handlers(up_router),
        *user.register_handlers(up_router, bot=kwargs['bot']),
        other_router
    )

    # other_router.message.middleware(ThrottlingMiddleware(rate_limit=10))

    up_router.include_routers(*routers)