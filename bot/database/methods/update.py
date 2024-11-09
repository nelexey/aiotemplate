from sqlalchemy.exc import NoResultFound
from bot.database.main import Database
from bot.database.models.user import User
from typing import Optional

def update_user(chat_id: int, username: Optional[str] = None) -> bool:
    """
    Updates the specified fields of a user record in the database by chat_id.

    Args:
        chat_id (int): The unique identifier for the user from Telegram.
        username (Optional[str]): The new username to set for the user, if provided.

    Returns:
        bool: True if the user was found and updated successfully, False if the user was not found.

    This template demonstrates updating user data, with flexibility to modify multiple fields.
    """
    session = Database().session

    try:
        # Locate the user by chat_id
        user = session.query(User).filter(User.chat_id == chat_id).one()

        # Update fields if new values are provided
        if username is not None:
            user.username = username

        # Commit changes
        session.commit()
        return True

    except NoResultFound:
        # Return False if the user does not exist in the database
        return False

    finally:
        session.close()
