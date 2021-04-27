import unittest
from app.models import Role
from app import db

class TestRole(unittest.TestCase):

    def setUp(self):
        self.new_role = Role(id=1, name=3)


    def test_instance(self):
        self.assertTrue(isinstance(self.new_role,Role))


