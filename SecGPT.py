from core.config import Config
from core.message import Message
from core.prompt import Prompt
from core.interactor import Interactor
from core.character import Character
from core.translate import Translator
from core.plugins import Plugins
from core.log import Log

import json

class SecGPTAgent:
    def __init__(self):
        self.logger = Log(__name__).get_logger()
        self.initialize_settings()
        self.initialize_managers()

    def initialize_settings(self):
        """Initialize settings."""
        self.name = ''
        self.desc = ''
        self.goals = []
        self.plugins = ''

    def initialize_managers(self):
        """Initialize all the managers and services."""
        try:
            self.config_manager = Config('config/config.yaml')
            api_key = self.config_manager.get('openai_key')
            self.interactor = Interactor(api_key)
            self.translator = Translator(api_key)
            self.message_manager = Message()
            self.character_manager = Character('prompts/character.yaml')
            self.character_manager_system = self.character_manager.get_character_info("system")
            self.character_manager_user = self.character_manager.get_character_info("user")
            self.prompt_manager = Prompt()
            self.plugins_manager = Plugins()
        except Exception as e:
            self.log_error(e)
            raise e

    def log_error(self, e):
        """Log errors."""
        self.logger.error(f"Error: {e}")

    # 初始化角色
    def init_character(self):
        """Initialize character."""
        try:
            user_input = input("Please input your goal: ")
            self.character_manager_user = self.character_manager.render_character_info("user", user_input)
            self.message_manager.add_message("system", self.character_manager_system)
            self.message_manager.add_message("user", self.character_manager_user)
            response = self.interactor.chat(self.message_manager.get_messages())
            self.name, self.desc, self.goals = self.character_manager.set_character_info(response)
            self.goal_str = '\n'.join(f'- {goal}' for goal in self.goals)
            # translated_desc = self.translator.translate(self.desc)
            # translated_goal_str = self.translator.translate(self.goal_str)
            # self.log_character_info(translated_desc, translated_goal_str)
        except Exception as e:
            self.log_error(e)
            raise e

    def log_character_info(self, translated_desc, translated_goal_str):
        """Log character information."""
        self.logger.info(f"Name: {self.name}")
        self.logger.info(f"Description: {self.desc}")
        self.logger.info(f"Goals: {self.goals}")
        self.logger.info(f"Translated Description: {translated_desc}")
        self.logger.info(f"Translated Goals: {translated_goal_str}")

    def init_prompt(self):
        """Initialize prompt."""
        try:
            self.retrieve_character_info_if_missing()
            self.plugins_manager.load_plugins()
            self.plugins = self.plugins_manager.gen_plugins_prompt()
            self.system_prompts = self.prompt_manager.gen_system_prompt(self.name, self.desc, self.goals, self.plugins)
            self.user_prompts = self.prompt_manager.gen_user_prompt()
            self.message_manager.clear_messages()
            self.message_manager.add_message("system", self.system_prompts)
            self.message_manager.add_message("user", self.user_prompts)
        except Exception as e:
            self.log_error(e)
            raise e

    def retrieve_character_info_if_missing(self):
        """Retrieve character information from store if missing."""
        if not self.name:
            self.name = self.character_manager.get_store_character_info()['name']
        if not self.desc:
            self.desc = self.character_manager.get_store_character_info()['description']
        if not self.goals:
            self.goals = self.character_manager.get_store_character_info()['goals']

    def process_command(self, json_data):
        """Process commands."""
        command = json_data['command']
        command_name = command['name']
        command_args = command['args']
        call_func = self.plugins_manager.call_plugin_func(command_name, command_args)
        self.logger.info(f"AI command execute: {call_func}")
        self.message_manager.add_message("assistant", json.dumps(json_data))
        self.message_manager.add_message("system", call_func)
        self.message_manager.add_message("user", self.prompt_manager.gen_user_prompt())

    def chat_loop(self):
        """Chat loop."""
        user_input = input("Do you want to create a new character? (y/n): ")
        if user_input == 'y':
            self.init_character()
        self.init_prompt()
        while True:
            self.process_chat_response()

    def process_chat_response(self):
        """Process chat response."""
        try:
            response = self.message_manager.json_validate(self.interactor.chat(self.message_manager.get_messages()))
            thoughts = response['thoughts']
            command = response['command']
            self.log_chat_response(thoughts, command)
            user_input = input(":")
            self.process_command(response)
        except Exception as e:
            self.log_error(e)
            raise e

    def log_chat_response(self, thoughts, command):
        """Log chat response."""
        text = thoughts['text']
        reasoning = thoughts['reasoning']
        plan = thoughts['plan']
        criticism = thoughts['criticism']
        speak = thoughts['speak']
        command_name = command['name']
        command_args = command['args']
        self.logger.info(f"AI thoughts: {text}")
        self.logger.info(f"AI reasoning: {reasoning}")
        self.logger.info(f"AI plan: {plan}")
        self.logger.info(f"AI criticism: {criticism}")
        self.logger.info(f"AI speak: {speak}")
        self.logger.info(f"AI command: {command_name} {command_args}")


if __name__ == "__main__":
    agent = SecGPTAgent()
    agent.chat_loop()
