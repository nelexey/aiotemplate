from typing import Final
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from bot.misc.env import settings

class Database:
    """
    Class responsible for configuring and managing the database connection.

    Attributes:
        BASE (Final): SQLAlchemy declarative base used to define models.
    """
    BASE: Final = declarative_base()

    def __init__(self):
        """
        Initializes the database connection using the URL from settings and creates a session.
        Note: No modifications are needed in this class; it's structured to handle database setup efficiently.
        """
        self.__engine = create_engine(settings.database_url)
        session = sessionmaker(bind=self.__engine)
        self.__session = session()

    @property
    def session(self):
        """Provides the current database session."""
        return self.__session

    @property
    def engine(self):
        """Provides access to the database engine."""
        return self.__engine
