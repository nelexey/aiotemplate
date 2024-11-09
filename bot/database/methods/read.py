from typing import Optional
from sqlalchemy.exc import NoResultFound
from bot.database.main import Database
from bot.database.models.user import User

def get_user(chat_id: int) -> Optional[User]:
    """
    Retrieves a user by their chat_id from the database.

    Args:
        chat_id (int): The unique identifier for the user from Telegram.

    Returns:
        Optional[User]: The user object if found; otherwise, None.

    This template demonstrates a basic approach to querying a user by `chat_id`.
    """
    try:
        # Query for a user by chat_id
        return Database().session.query(User).filter(User.chat_id == chat_id).one()
    except NoResultFound:
        # Return None if no user is found
        return None
