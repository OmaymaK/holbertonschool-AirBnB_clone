#!/user/bin/pyhton3
""" Base Model Class """
from datetime import datetime
import uuid


class BaseModel():
    """ Base Class """

    def __init__(self, *args, **kwargs):
        """ Initialization """
        if (kwargs):
            for i in kwargs:
                if i != "__class__":
                    if i != "created_at" and i != "updated_at":
                        setattr(self, i, kwargs[i])
                    else:
                        setattr(self, i, datetime.fromisoformat(kwargs[i]))

        else:
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
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
