from typing import List
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def create_reply_keyboard(data: List[str], row_width: int = 3) -> ReplyKeyboardMarkup:
    """
    Creates a reply keyboard markup with specified button texts and row width.

    Args:
        data (List[str]): A list of button texts for each button in the keyboard.
        row_width (int): The maximum number of buttons in each row. Default is 3.

    Returns:
        ReplyKeyboardMarkup: A reply keyboard markup object for use in messages.
    """
    # Generate reply keyboard markup by grouping buttons into rows according to row_width
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=item) for item in data[i:i + row_width]]
            for i in range(0, len(data), row_width)
        ],
        resize_keyboard=True  # Adjusts keyboard size to fit buttons neatly
    )
