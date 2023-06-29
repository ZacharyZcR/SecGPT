import unittest
from core.config import Config

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.config_manager = Config('../config/config.yaml')

    def test_get(self):
        openai_key = self.config_manager.get('openai_key')
        self.assertIsNotNone(openai_key)

if __name__ == "__main__":
    unittest.main()
