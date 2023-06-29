import unittest
from core.character import Character

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character_manager = Character('../prompts/character.yaml')

    def test_get_character_info(self):
        character_info = self.character_manager.get_character_info()
        self.assertIsNotNone(character_info)

if __name__ == "__main__":
    unittest.main()
