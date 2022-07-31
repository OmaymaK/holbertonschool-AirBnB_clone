#!/user/bin/pyhton3
""" Base Model Class """
from datetime import datetime
import uuid


class BaseModel():
    """ Base Class """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ prints string representation """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """ updates the public instance attribute """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary """
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = str(self.created_at.isoformat())
        self.__dict__["updated_at"] = str(self.updated_at.isoformat())
        return self.__dict__
