from aiohttp import web
from aiogram import Bot
from bot.web.urls import urls

class WebServer():
    def __init__(self, config: dict, bot: Bot):
        self.config = config
        self.bot = bot
        self.app = web.Application()
        self.setup_routes()

    def setup_routes(self):
        for route in urls:
            self.app.router.add_route(
                route['method'],
                route['path'],
                self.create_handler(route['handler'])
            )

    def create_handler(self, handler):
        async def wrapper(request):
            return await handler(request, self.bot)

        return wrapper

    async def run(self):
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


async def init_web_server(config: dict, bot: Bot):
    server = WebServer(config, bot)
    await server.run()