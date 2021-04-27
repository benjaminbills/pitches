import unittest
from app.models import Pitch, User, Comment
from app import db

class TestPitch(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(id=1, owner_id=3, description="Amazing day yo be alive",title='Flexing',category='Pickup Line')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))


