from typing import List, Tuple
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def create_inline_keyboard(data: List[Tuple[str, str]], row_width: int = 3) -> InlineKeyboardMarkup:
    """
    Creates an inline keyboard markup with specified button data and row width.

    Args:
        data (List[Tuple[str, str]]): A list of tuples where each tuple contains
            (button text, callback data) for each button.
        row_width (int): The maximum number of buttons in each row. Default is 3.

    Returns:
        InlineKeyboardMarkup: An inline keyboard markup object for use in messages.
    """
    # Generate inline keyboard markup by grouping buttons into rows according to row_width
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=text, callback_data=callback_data)
                for text, callback_data in data[i:i + row_width]
            ]
            for i in range(0, len(data), row_width)
        ]
    )
