import yaml
import re
from pathlib import Path
from core.log import Log
from utils.constants import CHARACTER_STORE_FILE_PATH, NAME_REGEX, DESCRIPTION_REGEX, GOALS_REGEX


class Character:
    def __init__(self, character_file):
        self.logger = Log(__name__).get_logger()
        self.character_file = Path(character_file)
        self.character_info = self._load_file(self.character_file)
        self.character_store_file = CHARACTER_STORE_FILE_PATH

    def _load_file(self, filepath):
        try:
            with open(filepath, 'r') as f:
                data = yaml.safe_load(f)
            self.logger.debug(f"Loaded file {filepath}")
            return data
        except Exception as e:
            self.logger.error(f"Failed to load file {filepath}. Error: {e}")
            return None

    def _write_file(self, filepath, content):
        try:
            with open(filepath, 'w') as f:
                yaml.dump(content, f)
            self.logger.debug(f"Wrote to file {filepath}")
        except Exception as e:
            self.logger.error(f"Failed to write to file {filepath}. Error: {e}")

    def get_character_info(self, role):
        return self.character_info.get(role)

    def render_character_info(self, role, user_input):
        template = self.get_character_info(role)
        return template.replace('{{user_prompt}}', user_input)

    def render_character_system_info(self, user_input):
        template = self.get_character_info('system')
        return template.replace('{{Commands}}', user_input)

    def set_character_info(self, text):
        try:
            name = re.search(NAME_REGEX, text, re.IGNORECASE).group(1)
            desc = re.search(DESCRIPTION_REGEX, text, re.IGNORECASE | re.DOTALL).group(1).strip()
            goals = re.findall(GOALS_REGEX, text)

            self.character_info = {'name': name, 'description': desc, 'goals': goals}
            self._write_file(self.character_store_file, self.character_info)
            self.logger.debug(f"Set character info: {self.character_info}")
            return name, desc, goals
        except Exception as e:
            self.logger.error(f"Failed to set character info. Error: {e}")
            raise e

    def get_store_character_info(self):
        return self._load_file(self.character_store_file)

