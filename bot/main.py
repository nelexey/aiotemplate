import asyncio
import logging
from aiogram import Bot, Dispatcher, Router

from bot.misc.env import settings
from bot.web.server import init_web_server
from bot.handlers.main import register_all_handlers

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    # Инициализация бота
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()

    try:

        # Запуск веб-сервера
        logger.info("Starting web server...")
        await init_web_server(settings.web_config, bot)
        logger.info(f"Web server started on {settings.web_config['host']}:{settings.web_config['port']}")

        # Запуск бота
        logger.info("Register bot handlers...")
        main_router = Router()
        await register_all_handlers(main_router)
        dp.include_router(main_router)

        logger.info("Starting bot...")
        await dp.start_polling(bot)

    except Exception as e:
        logger.error(f"Error occurred: {e}")
        await bot.session.close()

    finally:
        # Закрытие сессии бота при завершении
        await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")