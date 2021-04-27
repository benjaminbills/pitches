import unittest
from app.models import Upvote
from app import db

class TestUpvote(unittest.TestCase):

    def setUp(self):
        self.new_upvote = Upvote(id=1, user_id=3, pitch_id=10)


    def test_instance(self):
        self.assertTrue(isinstance(self.new_upvote,Upvote))


