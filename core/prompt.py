import yaml
from pathlib import Path
from core.log import Log
from utils.constants import PROMPT_DIRECTORY, JSON_SCHEMA_PROMPT, PROMPT_SECTIONS, USER_PROMPT

class Prompt:
    def __init__(self, prompt_dir=PROMPT_DIRECTORY):
        self.prompt_dir = Path(prompt_dir)
        if not self.prompt_dir.is_dir():
            raise FileNotFoundError(f"Prompt directory {self.prompt_dir} does not exist")
        self.logger = Log(__name__).get_logger()

    def _read_prompt(self, prompt_file):
        prompt_path = self.prompt_dir / f'{prompt_file}.yaml'
        if not prompt_path.is_file():
            self.logger.error(f"Prompt file {prompt_path} does not exist")
            return None
        return yaml.safe_load(prompt_path.read_text())

    def _gen_json_schema(self):
        try:
            json_schema = JSON_SCHEMA_PROMPT
            json_schema += str(self._read_prompt('json_schema'))
            self.logger.debug(f"Generated JSON schema: {json_schema}")
            return json_schema
        except Exception as e:
            self.logger.error(f"Failed to generate JSON schema. Error: {e}")
            return None

    def _gen_prompt_section(self, section_name, data=None):
        if data is None:
            data = self._read_prompt(section_name.lower().replace(' ', '_'))
        section = f'{section_name}:\n' + '\n'.join(f'{item}' for item in data)
        return section + '\n'

    def gen_system_prompt(self, name, desc, goals, plugins):
        try:
            prompts = f"You are {name}, {desc}\n"
            prompts += "Your decisions must always be made independently without seeking user assistance. " \
                       "Play to your strengths as an LLM and pursue simple strategies with no legal complications.\n"
            sections = PROMPT_SECTIONS
            data = [goals] + [None] * (len(sections) - 1)

            for section, data in zip(sections, data):
                if section == 'Commands':
                    prompts += plugins
                else:
                    prompts += self._gen_prompt_section(section, data)

            prompts += self._gen_json_schema()  # Add json_schema to the prompts
            self.logger.debug(f"Generated system prompts: {prompts}")
            return prompts
        except Exception as e:
            self.logger.error(f"Failed to generate system prompts. Error: {e}")
            return None

    def gen_user_prompt(self):
        return USER_PROMPT

if __name__ == "__main__":
    prompt = Prompt(prompt_dir='../prompts/')
    system_prompt = prompt.gen_system_prompt('test', 'test', ['test1', 'test2'])
    print(system_prompt)
