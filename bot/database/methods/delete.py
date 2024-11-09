from sqlalchemy.exc import NoResultFound
from bot.database.main import Database
from bot.database.models.user import User

def delete_user(chat_id: int) -> bool:
    """
    Deletes a user from the database by chat_id.

    Args:
        chat_id (int): The unique identifier for the user from Telegram.

    Returns:
        bool: True if the user was found and deleted successfully, False if the user was not found.

    This template demonstrates deleting a user based on the provided `chat_id`.
    """
    session = Database().session

    try:
        # Locate the user by chat_id
        user = session.query(User).filter(User.chat_id == chat_id).one()

        # Delete the user from the session
        session.delete(user)

        # Commit changes to persist the deletion
        session.commit()
        return True

    except NoResultFound:
        # Return False if the user does not exist in the database
        return False

    finally:
        session.close()
