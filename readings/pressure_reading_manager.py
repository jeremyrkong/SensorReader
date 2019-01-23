# This script represents the Pressure Reading Manager class
#
# Author: Derek Wong
# Version 1.0
from readings.abstract_reading_manager import AbstractReadingManager
from readings.pressure_reading import PressureReading
import datetime

class PressureReadingManager(AbstractReadingManager):
    """ Concrete Implementation of a Pressure Reading Manager """

    NUM = "SEQUENCE NUM"
    NAME = "SENSOR NAME"
    MIN_READING = "MINIMUM READING"
    AVERAGE_READING = "AVERAGE READING"
    MAX_READING = "MAXIMUM READING"
    READING_STATUS = "STATUS"

    def add_log_message(self, model, min_reading, avg_reading, max_reading, status):
        """ Add a log message to the database """
        
        PressureReadingManager._validate_input(PressureReadingManager.NAME, model)
        PressureReadingManager._validate_input(PressureReadingManager.MIN_READING, min_reading)
        PressureReadingManager._validate_input(PressureReadingManager.AVERAGE_READING, avg_reading)
        PressureReadingManager._validate_input(PressureReadingManager.MAX_READING, max_reading)
        PressureReadingManager._validate_input(PressureReadingManager.READING_STATUS, status)
        
        session = self.DBSession()
        new_log_message = PressureReading(model, min_reading, avg_reading, max_reading, status)
        session.add(new_log_message)
        session.commit()

    def delete_log_message(self, id):
        """ Remove a log message from the DB based on its Id """
    
        PressureReadingManager._validate_input(PressureReadingManager.NUM, id)
        PressureReadingManager._validate_float(PressureReadingManager.NUM, id)
        
        session = self.DBSession()
        if session.query(PressureReading).filter(PressureReading.id == id).first():
            log_message = session.query(PressureReading).filter(PressureReading.id == id).first()
            session.delete(log_message)
            session.commit()
            return True
        return False

    def get_log_message(self, id):
        """ Gets and returns a log message from the DB based on its Id """
        
        PressureReadingManager._validate_input(PressureReadingManager.NUM, id)
        PressureReadingManager._validate_float(PressureReadingManager.NUM, id)
        
        session = self.DBSession()
        if session.query(PressureReading).filter(PressureReading.id == id).first():
            session.commit()
            return session.query(PressureReading).filter(PressureReading.id == id).first()
        return None

    def get_log_messages(self):
        """ Gets and returns all log messages in the DB """
        session = self.DBSession()
        log_messages = session.query(PressureReading).all()
        log_list = []

        for log in log_messages:
            log_list.append(log)

        session.commit()
        return log_list

    def update_log_message(self, id, model, min_reading, avg_reading, max_reading, status):
        """" Updates a log message based on its id """

        PressureReadingManager._validate_input(PressureReadingManager.NUM, id)
        PressureReadingManager._validate_input(PressureReadingManager.NAME, model)
        PressureReadingManager._validate_input(PressureReadingManager.MIN_READING, min_reading)
        PressureReadingManager._validate_input(PressureReadingManager.AVERAGE_READING, avg_reading)
        PressureReadingManager._validate_input(PressureReadingManager.MAX_READING, max_reading)
        PressureReadingManager._validate_input(PressureReadingManager.READING_STATUS, status)
        PressureReadingManager._validate_string(PressureReadingManager.NAME, model)
        PressureReadingManager._validate_string(PressureReadingManager.READING_STATUS, status)
        PressureReadingManager._validate_float(PressureReadingManager.NUM, id)
        PressureReadingManager._validate_float(PressureReadingManager.MIN_READING, min_reading)
        PressureReadingManager._validate_float(PressureReadingManager.AVERAGE_READING, avg_reading)
        PressureReadingManager._validate_float(PressureReadingManager.MAX_READING, max_reading)
        
        session = self.DBSession()
        new_log = session.query(PressureReading).filter(PressureReading.id == id).first()
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

    @staticmethod
    def _validate_string(display_name, input_value):
        """ Private method to validate the input value is a string type """

        if str(input_value) is False:
            raise ValueError(display_name + " must be a string type")

    @staticmethod
    def _validate_float(display_name, input_value):
        """ Private method to validate the input value is a float type """

        if float(input_value) is False:
            raise ValueError(display_name + " must be a float type")

    @staticmethod
    def _validate_int(display_name, input_value):
        """ Private method to validate input value is a integer type """

        if int(input_value) is False:
            raise ValueError(display_name + "must be a integer type")

