#
# This is a script to read in and process temperature sensor readings
#
# Author: Joe Developer
# Version: 1.0
#

from readings.temperature_reading_manager import TemperatureReadingManager
from readings.temperature_reading import TemperatureReading
from readings.pressure_reading_manager import PressureReadingManager
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from sqlalchemy_declarative import Base


def create_sensors_and_readings():
    """ Populates the Database """

    temperature_reading_manager = TemperatureReadingManager()
    temperature_reading_manager.add_log_message(model="ABC Sensor Temp M301A", min_reading=20.212, avg_reading=21.367, max_reading=22.005, status="OK")
    pressure_reading_manager = PressureReadingManager()
    pressure_reading_manager.add_log_message(model="ABC Sensor Pres M100", min_reading=50.163, avg_reading=51.435, max_reading=52.103, status="GOOD")


def main():
    """ Main Function - Populate DB """

    create_sensors_and_readings()


if __name__ == "__main__":
    main()
