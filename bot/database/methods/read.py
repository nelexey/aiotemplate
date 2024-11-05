from typing import Optional
from sqlalchemy import exc

from bot.database.main import Database
from bot.database.models.user import User


def get_user(chat_id: int) -> Optional[User]:
    """Get user by chat_id"""

    try:
        return Database().session.query(User).filter(User.chat_id == chat_id).one()
    except exc.NoResultFound:
        return None