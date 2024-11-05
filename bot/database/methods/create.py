from sqlalchemy.exc import NoResultFound

from bot.database.main import Database
from bot.database.models.user import User

def create_user(chat_id: int, username: str) -> None:
    """Add user in database if not exists"""

    session = Database().session

    try:
        session.query(User.chat_id).filter(User.chat_id == chat_id).one()

    except NoResultFound:
        new_user = User(
            chat_id=chat_id,
            username=username,
        )
        session.add(new_user)

        session.commit()