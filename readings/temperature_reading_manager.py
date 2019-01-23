# This script represents the Temperature Reading Manager class
#
# Author: Derek Wong
# Version 1.0
from readings.abstract_reading_manager import AbstractReadingManager
from readings.temperature_reading import TemperatureReading
import datetime

class TemperatureReadingManager(AbstractReadingManager):
    """ Concrete Implementation of a Temperature Reading Manager """

    NUM = "SEQUENCE NUM"
    NAME = "SENSOR NAME"
    MIN_READING = "MINIMUM READING"
    AVERAGE_READING = "AVERAGE READING"
    MAX_READING = "MAXIMUM READING"
    READING_STATUS = "STATUS"

    def add_log_message(self, model, min_reading, avg_reading, max_reading, status):
        """ Add a log message to the database """

        TemperatureReadingManager._validate_input(TemperatureReadingManager.NAME, model)
        TemperatureReadingManager._validate_input(TemperatureReadingManager.MIN_READING, min_reading)
        TemperatureReadingManager._validate_input(TemperatureReadingManager.AVERAGE_READING, avg_reading)
        TemperatureReadingManager._validate_input(TemperatureReadingManager.MAX_READING, max_reading)
        TemperatureReadingManager._validate_input(TemperatureReadingManager.READING_STATUS, status)

        session = self.DBSession()
        new_log_message = TemperatureReading(model, min_reading, avg_reading, max_reading, status)
        session.add(new_log_message)
        session.commit()

    def delete_log_message(self, id):
        """ Remove a log message from the DB based on its Id """

        TemperatureReadingManager._validate_input(TemperatureReadingManager.NUM, id)

        session = self.DBSession()
        if session.query(TemperatureReading).filter(TemperatureReading.id == id).first():
            log_message = session.query(TemperatureReading).filter(TemperatureReading.id == id).first()
            session.delete(log_message)
            session.commit()
            return True
        return False

    def get_log_message(self, id):
        """ Gets and returns a log message from the DB based on its Id """

        TemperatureReadingManager._validate_input(TemperatureReadingManager.NUM, id)

        session = self.DBSession()
        if session.query(TemperatureReading).filter(TemperatureReading.id == id).first():
            session.commit()
            return session.query(TemperatureReading).filter(TemperatureReading.id == id).first()
        return None

    def get_log_messages(self):
        """ Gets and returns all log messages in the DB """
        session = self.DBSession()
        log_messages = session.query(TemperatureReading).all()
        log_list = []

        for log in log_messages:
            log_list.append(log)
        session.commit()
        return log_list

    def update_log_message(self, id, model, min_reading, avg_reading, max_reading, status):
        """" Updates a log message based on its id """

        TemperatureReadingManager._validate_input(TemperatureReadingManager.NUM, id)
        TemperatureReadingManager._validate_input(TemperatureReadingManager.NAME, model)
        TemperatureReadingManager._validate_input(TemperatureReadingManager.MIN_READING, min_reading)
        TemperatureReadingManager._validate_input(TemperatureReadingManager.AVERAGE_READING, avg_reading)
        TemperatureReadingManager._validate_input(TemperatureReadingManager.MAX_READING, max_reading)
        TemperatureReadingManager._validate_input(TemperatureReadingManager.READING_STATUS, status)

        session = self.DBSession()
        new_log = session.query(TemperatureReading).filter(TemperatureReading.id == id).first()
        new_log.timestamp = datetime.datetime.now()
        new_log.model = model
        new_log.min_reading = min_reading
        new_log.avg_reading = avg_reading
        new_log.max_reading = max_reading
        new_log.status = status
        session.commit()


    @staticmethod
    def _validate_input(display_name, input_value):
        """ Private helper to validate input values as not None or an empty string """

        if input_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if input_value == "":
            raise ValueError(display_name + " cannot be empty.")