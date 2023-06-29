import os
import openai
from core.log import Log

class Translator:
    def __init__(self, api_key, model="gpt-3.5-turbo", src_lang="English", tgt_lang="Chinese"):
        self.logger = Log(__name__).get_logger()
        openai.api_key = api_key
        self.model = model
        self.src_lang = src_lang
        self.tgt_lang = tgt_lang

    def translate(self, text):
        messages = []
        messages.append({"role": "system", "content": f"You are a translator, translate {self.src_lang} to {self.tgt_lang}, just get the translation result."})
        messages.append({"role": "user", "content": text})
        try:
            response = openai.ChatCompletion.create(model=self.model, messages=messages)
            self.logger.debug(f"Response: {response}")
            return response['choices'][0]['message']['content']
        except Exception as e:
            self.logger.error(f"Error: {e}")
            print(f"Error: {e}")
