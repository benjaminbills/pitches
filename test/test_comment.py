import unittest
from app.models import Pitch, User, Comment
from app import db

class TestComment(unittest.TestCase):

    def setUp(self):
        self.new_comment = Comment(id=1,pitch_id=4,user_id=3,description='Driving on a fast lane')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))


