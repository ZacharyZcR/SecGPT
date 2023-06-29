import unittest
from core.interactor import Interactor
from core.message import Message
from core.config import Config

class TestInteractor(unittest.TestCase):
    def setUp(self):
        openai_key = Config('../config/config.yaml').get('openai_key')
        self.interactor = Interactor(openai_key)

    def test_chat(self):
        message_manager = Message()
        message_manager.add_message("user", "Hello, world!")
        assistant_message = self.interactor.chat(message_manager.get_messages())
        self.assertIsNotNone(assistant_message)

if __name__ == "__main__":
    unittest.main()
