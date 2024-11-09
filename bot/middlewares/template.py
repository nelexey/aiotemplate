from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from typing import Any, Awaitable, Callable, Dict

class TemplateMiddleware(BaseMiddleware):
    """
    A template middleware example for handling events in aiogram with additional processing.

    Args:
        some_parameter (str): A customizable parameter that can be used within the middleware logic.
    """

    def __init__(self, some_parameter: str) -> None:
        self.some_parameter = some_parameter

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        """
        Middleware function that processes events and calls the appropriate handler.

        Args:
            handler (Callable): The next handler to be called in the middleware chain.
            event (TelegramObject): The event data (e.g., a message).
            data (Dict[str, Any]): Additional data passed to the handler.

        Returns:
            Any: The result of the handler execution.
        """
        # Middleware logic
        if isinstance(event, Message):
            # Perform additional processing if the event is a Message
            # For example, logging or modifying data
            pass

        # Call the handler if all conditions are met
        return await handler(event, data)
