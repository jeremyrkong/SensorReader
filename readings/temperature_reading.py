from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from readings.abstract_reading import AbstractReading

import json
import datetime

class TemperatureReading(AbstractReading):
    """ Temperature Reading Table """

    NUM = "SEQUENCE NUM"
    NAME = "SENSOR NAME"
    MIN_READING = "MINIMUM TEMPERATURE"
    AVERAGE_READING = "AVERAGE PRESSURE"
    MAX_READING = "MAXIMUM TEMPERATURE"
    READING_STATUS = "STATUS"

    __tablename__ = 'temperature_reading'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.now)
    model = Column(String(250))
    min_reading = Column(Float, nullable=False)
    avg_reading = Column(Float, nullable=False)
    max_reading = Column(Float, nullable=False)
    status = Column(String(250))

    def __init__(self, model, min_reading, avg_reading, max_reading, status):
        """Constructor for the abstract reading class"""

        # TemperatureReading._validate_input(TemperatureReading.NAME, model)
        # TemperatureReading._validate_input(TemperatureReading.MIN_READING, min_reading)
        # TemperatureReading._validate_input(TemperatureReading.AVERAGE_READING, avg_reading)
        # TemperatureReading._validate_input(TemperatureReading.MAX_READING, max_reading)
        # TemperatureReading._validate_input(TemperatureReading.READING_STATUS, status)

        self.model = model
        self.min_reading = min_reading
        self.avg_reading = avg_reading
        self.max_reading = max_reading
        self.status = status

    def to_json(self):
        """Method to convert the data objects to JSON and return as response to service"""
        data = {
            "id": self.id,
            "timestamp": self.timestamp.strftime('%Y/%m/%d %H:%M:%S.%f'),
            "model": self.model,
            "min_reading": self.min_reading,
            "avg_reading": self.avg_reading,
            "max_reading": self.max_reading,
            "status": self.status
        }

        json_string = json.dumps(data, indent=4)
        return json_string

    def to_dict(self):
        """Method to convert the data objects to key value pairs in a dictionary and return as response to service"""
        data = {
            "id": self.id,
            "timestamp": self.timestamp.strftime('%Y/%m/%d %H:%M:%S.%f'),
            "model": self.model,
            "min_reading": self.min_reading,
            "avg_reading": self.avg_reading,
            "max_reading": self.max_reading,
            "status": self.status
        }

        return data

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

        if input_value != str(input_value):
            raise ValueError(display_name + " must be a string type")

    @staticmethod
    def _validate_float(display_name, input_value):
        """ Private method to validate the input value is a float type """

        if input_value != float(input_value):
            raise ValueError(display_name + " must be a float type")

    @staticmethod
    def _validate_int(display_name, input_value):
        """ Private method to validate input value is a integer type """

        if input_value != int(input_value):
            raise ValueError(display_name + "must be a integer type")

