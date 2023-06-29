import json
import re
from core.log import Log

class Message:
    def __init__(self):
        self.logger = Log(__name__).get_logger()
        self.messages = []

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})

    def get_messages(self):
        return self.messages

    def clear_messages(self):
        self.messages = []

    def json_validate(self, json_str):
        try:
            data = json.loads(json_str)
            self.logger.debug(f"JSON: {data}")
            return data
        except Exception as e:
            self.logger.error(f"Error: {e}")
            return self.extract_json(json_str)


    def extract_json(self, str):
        try:
            # 使用正则表达式匹配json格式的数据
            json_str = re.search(r'\{.*\}', str).group()
            self.logger.debug(f"JSON: {json_str}")
            # 解析json数据
            json_data = json.loads(json_str)
            return json_data
        except Exception as e:
            self.logger.error(f"Error: {e}")
            return None

