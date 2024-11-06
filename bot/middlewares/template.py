from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from typing import Any, Awaitable, Callable, Dict


class TemplateMiddleware(BaseMiddleware):
    def __init__(self, some_parameter: str):
        self.some_parameter = some_parameter

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        # Логика миддлвейра
        if isinstance(event, Message):
            # Дополнительная обработка события, если это сообщение
            pass

        # Вызов обработчика, если все в порядке
        return await handler(event, data)
