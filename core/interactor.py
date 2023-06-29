import openai
from core.log import Log

class Interactor:
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        if not api_key:
            raise ValueError("API key is required.")
        openai.api_key = api_key
        self.model = model
        self.logger = Log(__name__).get_logger()

    def chat(self, messages):
        if not messages:
            raise ValueError("Messages are required.")
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages
            )
            self.logger.debug(f"Response: {response}")
            return response.choices[0].message.content
        except Exception as e:
            self.logger.error(f"Error: {e}")
            raise e
