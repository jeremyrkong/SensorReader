# This script tests the Temperature Reading Manager class
#
# Author: Derek Wong
# Version 1.0
import unittest
from unittest import TestCase
from unittest.mock import MagicMock
from unittest.mock import patch, mock_open
from readings.temperature_reading_manager import TemperatureReadingManager
from readings.pressure_reading_manager import PressureReadingManager
import csv
import datetime
import inspect
import os
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class TestTemperatureReadingManager(TestCase):
    """ Unit Tests for the Temperature Reading Manager Class """

    TEST_DB = 'readings.sqlite'

    def setUp(self):
        """ Creates a test database fixture before each test method is run """
        self.logPoint()

        conn = sqlite3.connect("readings.sqlite")

        c = conn.cursor()
        c.execute('''
             CREATE TABLE temperature_reading
             (id INTEGER PRIMARY KEY ASC,
              timestamp DATETIME NOT NULL,
              model VARCHAR(250) NOT NULL,
              min_reading NUMBER NOT NULL,
              avg_reading NUMBER NOT NULL,
              max_reading NUMBER NOT NULL,
              status VARCHAR(250) NOT NULL
             )
             ''')
        c.execute('''
             CREATE TABLE pressure_reading
             (id INTEGER PRIMARY KEY ASC,
              timestamp DATETIME NOT NULL,
              model VARCHAR(250) NOT NULL,
              min_reading NUMBER NOT NULL,
              avg_reading NUMBER NOT NULL,
              max_reading NUMBER NOT NULL,
              status VARCHAR(250) NOT NULL
             )
             ''')

        conn.commit()
        conn.close()

        self.test_temperature_reading_manager = TemperatureReadingManager()


    def test_valid_add_log_message(self):
        """010A - Valid add log message """
        self.assertIsNone(self.test_temperature_reading_manager.add_log_message(model="ABC Sensor Temp M301A",
                                                              min_reading=20.152,
                                                              avg_reading=21.367,
                                                              max_reading=22.005,
                                                              status="OK"))

    def test_invalid_add_log_message(self):
        """010B - Invalid add log message """

        #Test for None
        with self.assertRaises(ValueError):
            self.test_temperature_reading_manager.add_log_message(model=None,
                                                              min_reading=20.152,
                                                              avg_reading=21.367,
                                                              max_reading=22.005,
                                                              status="OK")
            self.test_temperature_reading_manager.add_log_message(model="ABC Sensor Temp M301A",
                                                              min_reading=None,
                                                              avg_reading=21.367,
                                                              max_reading=22.005,
                                                              status="OK")
            self.test_temperature_reading_manager.add_log_message(model="ABC Sensor Temp M301A",
                                                              min_reading=20.152,
                                                              avg_reading=None,
                                                              max_reading=22.005,
                                                              status="OK")
            self.test_temperature_reading_manager.add_log_message(model="ABC Sensor Temp M301A",
                                                              min_reading=20.152,
                                                              avg_reading=21.367,
                                                              max_reading=None,
                                                              status="OK")
            self.test_temperature_reading_manager.add_log_message(model="ABC Sensor Temp M301A",
                                                              min_reading=20.152,
                                                              avg_reading=21.367,
                                                              max_reading=22.005,
                                                              status=None)

        #Test for empty string
        with self.assertRaises(ValueError):
            self.test_temperature_reading_manager.add_log_message(model="",
                                                              min_reading=20.152,
                                                              avg_reading=21.367,
                                                              max_reading=22.005,
                                                              status="OK")
            self.test_temperature_reading_manager.add_log_message(model="ABC Sensor Temp M301A",
                                                              min_reading="",
                                                              avg_reading=21.367,
                                                              max_reading=22.005,
                                                              status="OK")
            self.test_temperature_reading_manager.add_log_message(model="ABC Sensor Temp M301A",
                                                              min_reading=20.152,
                                                              avg_reading="",
                                                              max_reading=22.005,
                                                              status="OK")
            self.test_temperature_reading_manager.add_log_message(model="ABC Sensor Temp M301A",
                                                              min_reading=20.152,
                                                              avg_reading=21.367,
                                                              max_reading="",
                                                              status="OK")
            self.test_temperature_reading_manager.add_log_message(model="ABC Sensor Temp M301A",
                                                              min_reading=20.152,
                                                              avg_reading=21.367,
                                                              max_reading=22.005,
                                                              status="")

    def test_valid_delete_log_message(self):
        """020A - Valid log deletion """
        self.test_temperature_reading_manager.add_log_message(model="ABC Sensor Temp M301A",
                                                              min_reading=20.152,
                                                              avg_reading=21.367,
                                                              max_reading=22.005,
                                                              status="OK")

    def test_invalid_delete_log_message(self):
        """020B - Invalid log deletion """
        self.test_temperature_reading_manager.add_log_message(model="ABC Sensor Temp M301A",
                                                              min_reading=21.152,
                                                              avg_reading=21.367,
                                                              max_reading=23.005,
                                                              status="OK")

    def test_valid_get_log_message(self):
        """030A - Valid get log message by id """
        self.test_temperature_reading_manager.add_log_message(model="ABC Sensor Temp M301A",
                                                              min_reading=20.152,
                                                              avg_reading=21.367,
                                                              max_reading=22.005,
                                                              status="OK")

    def tearDown(self):
        """ Prints a log point when test is finished """
        self.logPoint()
        os.remove("readings.sqlite")

    def logPoint(self):
        """ Utility function used for module functions and class methods """
        current_test = self.id().split('.')[-1]
        calling_function = inspect.stack()[1][3]
        print('in %s - %s()' % (current_test, calling_function))

    if __name__ == "__main__":
        unittest.main()
