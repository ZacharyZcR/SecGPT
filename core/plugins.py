import os
import importlib
from core.log import Log
from utils.constants import PLUGIN_DIRECTORY, PYTHON_FILE_EXTENSION, COMMANDS_PROMPT


class Plugins:
    def __init__(self, plugin_directory=PLUGIN_DIRECTORY):
        self.logger = Log(__name__).get_logger()
        if not os.path.exists(plugin_directory):
            self.logger.error(f"Plugin directory does not exist: {plugin_directory}")
            raise FileNotFoundError(f"Plugin directory does not exist: {plugin_directory}")
        self.plugin_directory = plugin_directory
        self.plugins = {}

    def load_plugins(self):
        files = os.listdir(self.plugin_directory)
        for file in files:
            if file.endswith(PYTHON_FILE_EXTENSION):
                module_name = file[:-3]  # remove .py extension
                try:
                    module = importlib.import_module(f"{self.plugin_directory}.{module_name}")
                    if hasattr(module, "register"):
                        plugin_info = module.register()
                        self.plugins[plugin_info['name']] = plugin_info
                    self.logger.debug(f"Loaded plugin: {module_name}")
                except Exception as e:
                    self.logger.error(f"Failed to load plugin {module_name}. Error: {e}")
        self.logger.debug(f"Plugins: {self.plugins}")

    def get_plugins(self):
        return self.plugins

    def list_plugins(self):
        return list(self.plugins.keys())

    def gen_plugins_prompt(self):
        try:
            plugins_prompt = COMMANDS_PROMPT
            for i, plugin in enumerate(self.plugins.values(), 1):
                args_str = ', '.join([f'"{arg["name"]}": "<{arg["name"]}_string>"' for arg in plugin['args']])
                plugins_prompt += f"{plugin['name']}: {plugin['description']}, args: {args_str}\n"
            self.logger.debug(f"Plugins prompt: {plugins_prompt}")
            return plugins_prompt
        except Exception as e:
            self.logger.error(f"Error: {e}")
            raise e

    def call_plugin_func(self, plugin_name, args):
        try:
            self.logger.info(f"Call plugin: {plugin_name}")
            self.logger.info(f"args: {args}")
            plugin = self.plugins[plugin_name]
            return plugin['func'](args)
        except Exception as e:
            self.logger.error(f"Error: {e}")
            raise e