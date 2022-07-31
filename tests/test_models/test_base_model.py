#!/usr/bin/python3
import sys
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_id(self):
        self.model1 = BaseModel()
        self.model2 = BaseModel()
        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_update(self):
        self.model1 = BaseModel()
        update = self.model1.updated_at
        self.model1.save()
        self.assertNotEqual(self.model1.updated_at, update)

    def test_to_dict(self):
       model = BaseModel()
       dictt = model.to_dict()
       self.assertNotEqual(dictt, {})

if __name__ == '__main__':
    unittest.main()
