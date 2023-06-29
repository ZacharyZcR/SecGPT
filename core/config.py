import os
import yaml
from core.log import Log

class Config:
    def __init__(self, config_file):
        self.logger = Log(__name__).get_logger()
        if not os.path.exists(config_file):
            self.logger.error(f"Config file does not exist: {config_file}")
            raise FileNotFoundError(f"Config file does not exist: {config_file}")
        try:
            with open(config_file, 'r') as f:
                self.config = yaml.safe_load(f)
            self.logger.debug(f"Config: {self.config}")
        except Exception as e:
            self.logger.error(f"Error: {e}")
            raise e

    def get(self, key):
        return self.config.get(key)
