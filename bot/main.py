import asyncio
import logging
from aiogram import Bot, Dispatcher, Router

from bot.misc.env import settings
from bot.web.server import init_web_server
from bot.handlers.main import register_all_handlers
from bot.database.models import register_models

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main() -> None:
    """
    Initializes and starts the bot, setting up web server and handler registration.
    """
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()

    try:
        # Start web server
        logger.info("Starting web server...")
        await init_web_server(settings.web_config, bot)
        logger.info(f"Web server started on {settings.web_config['host']}:{settings.web_config['port']}")

        # Register bot handlers
        logger.info("Registering bot handlers...")
        main_router = Router()
        await register_all_handlers(main_router, bot=bot)
        dp.include_router(main_router)

        # Start polling
        logger.info("Starting bot polling...")
        await dp.start_polling(bot)

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        await bot.session.close()

    finally:
        # Ensure bot session closes when program ends
        await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
