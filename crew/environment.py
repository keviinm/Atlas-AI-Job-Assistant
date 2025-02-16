import os
from utils.helpers import get_openai_api_key, get_serper_api_key

class CrewEnvironment:
    """Configures API keys and environment variables."""
    @staticmethod
    def configure():
        os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'
        os.environ["SERPER_API_KEY"] = get_serper_api_key()