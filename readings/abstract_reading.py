from readings.base import Base

class AbstractReading(Base):
    """ Abstract Reading Class that map to the table in the sqlite database """

    __abstract__ = True