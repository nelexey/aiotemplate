from typing import Any, Awaitable, Callable, Dict
from datetime import datetime, timedelta
from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, rate_limit: int = 5):
        self.rate_limit = rate_limit
        self.user_timestamps = {}

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]) -> Any:
        user_id = event.from_user.id
        current_time = datetime.now()

        if user_id in self.user_timestamps:
            last_time = self.user_timestamps[user_id]
            time_diff = current_time - last_time
            if time_diff < timedelta(seconds=self.rate_limit):
                return await event.answer(f'Подождите {self.rate_limit - time_diff.seconds} секунд перед отправкой следующего сообщения.')

        self.user_timestamps[user_id] = current_time
        return await handler(event, data)
