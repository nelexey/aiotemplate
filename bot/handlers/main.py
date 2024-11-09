from aiogram import Router
from bot.handlers import user, admin
from .other import other_router
# from bot.middlewares.throttling import ThrottlingMiddleware

async def register_all_handlers(up_router: Router, **kwargs) -> None:
    """
    Registers all handler routers into the main application router.

    Args:
        up_router (Router): The main router where all sub-routers will be registered.
        **kwargs: Additional keyword arguments, such as `bot`, required by specific handlers.

    Notes:
        Uncomment the throttling middleware line to apply rate-limiting to `other_router`.
    """
    # Collect all routers to be included in the main router
    routers = (
        *admin.register_handlers(up_router),  # Register admin-specific handlers
        *user.register_handlers(up_router, bot=kwargs['bot']),  # Register user-specific handlers
        other_router  # Add other custom router
    )

    # Apply optional throttling middleware to limit message rate
    # other_router.message.middleware(ThrottlingMiddleware(rate_limit=10))

    # Include all routers in the main application router
    up_router.include_routers(*routers)
