import unittest
from core.prompt import Prompt

class TestPrompt(unittest.TestCase):
    def setUp(self):
        self.prompt_manager = Prompt('../prompts/constraints.yaml')

    def test_get_prompts(self):
        prompts = self.prompt_manager.get_prompts()
        self.assertIsNotNone(prompts)

if __name__ == "__main__":
    unittest.main()
