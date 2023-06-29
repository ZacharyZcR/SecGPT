import unittest
from core.message import Message

class TestMessage(unittest.TestCase):
    def setUp(self):
        self.message_manager = Message()

    def test_add_message(self):
        self.message_manager.add_message("user", "Hello, world!")
        messages = self.message_manager.get_messages()
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]["role"], "user")
        self.assertEqual(messages[0]["content"], "Hello, world!")

if __name__ == "__main__":
    unittest.main()
