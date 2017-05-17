import unittest
from api.watson import Conversation

class TestMessage(unittest.TestCase):
    def test_watson(self):

        c = Conversation()
        res = c.send_message(message="")

        print(res['output']['text'])
