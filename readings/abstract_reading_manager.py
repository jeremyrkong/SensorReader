from readings.abstract_reading import AbstractReading

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class AbstractReadingManager:
    """ Abstract Reading Manager Class """

    DB_NAME = 'sqlite:///readings.sqlite'

    def __init__(self):
        """ Create a SQLAlchemy engine and a DB Session Maker given a SQLite database filename """
        self.engine = create_engine(AbstractReadingManager.DB_NAME)
        self.DBSession = sessionmaker(bind=self.engine)

    def add_log_message(self, model, min_reading, avg_reading, max_reading, status):
        """ Abstract Method to add a log message to the database """
        raise NotImplementedError("Subclass must implement abstract method")

    def delete_log_message(self, id):
        """ Abstract Method to remove a log message from the DB based on its Id """
        session = self.DBSession()
        raise NotImplementedError("Subclass must implement abstract method")

    def get_log_message(self, id):
        """ Abstract Method to get and return a log message from the DB based on its Id """
        raise NotImplementedError("Subclass must implement abstract method")

    def get_log_messages(self):
        """ Abstract Method to get and return all log messages in the DB """
        raise NotImplementedError("Subclass must implement abstract method")

