import unittest
from app.models import Downvote
from app import db

class TestDownvote(unittest.TestCase):

    def setUp(self):
        self.new_downvote = Downvote(id=1, user_id=3, pitch_id=10)


    def test_instance(self):
        self.assertTrue(isinstance(self.new_downvote,Downvote))


