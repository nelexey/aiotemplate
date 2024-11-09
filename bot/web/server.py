from typing import Callable, Awaitable
from aiohttp import web
from aiogram import Bot

from bot.web.urls import urls


class WebServer:
    def __init__(self, config: dict, bot: Bot) -> None:
        """
        Initialize the web server with configuration settings and a bot instance.

        Args:
            config (dict): Configuration for the web server including host, port, and other settings.
            bot (Bot): An instance of the bot to be used in handlers.
        """
        self.config = config
        self.bot = bot
        self.app = web.Application()
        self.setup_routes()

    def setup_routes(self) -> None:
        """
        Sets up routes defined in the `urls` list, binding each path to its handler.
        """
        for route in urls:
            self.app.router.add_route(
                route['method'],
                route['path'],
                self.create_handler(route['handler'])
            )

    def create_handler(self, handler: Callable[[web.Request, Bot], Awaitable[web.Response]]) -> Callable[
        [web.Request], Awaitable[web.Response]]:
        """
        Wraps the handler to pass the bot instance as an argument.

        Args:
            handler (Callable): An asynchronous function that processes requests and interacts with the bot.

        Returns:
            Callable: A wrapper function for the handler with the bot as a parameter.
        """

        async def wrapper(request: web.Request) -> web.Response:
            return await handler(request, self.bot)

        return wrapper

    async def run(self) -> None:
        """
        Starts the web server with configurations provided during initialization.
        """
        runner = web.AppRunner(self.app)
        await runner.setup()
        site = web.TCPSite(
            runner,
            self.config['host'],
            self.config['port'],
            shutdown_timeout=self.config['timeout'],
            backlog=self.config['max_connections']
        )
        await site.start()


async def init_web_server(config: dict, bot: Bot) -> None:
    """
    Initializes and starts the web server with the given configuration and bot instance.

    Args:
        config (dict): Configuration settings for the server, including host and port.
        bot (Bot): Bot instance to be accessible to request handlers.
    """
    server = WebServer(config, bot)
    await server.run()
