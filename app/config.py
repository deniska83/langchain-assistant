import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot API token
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Twilio account SID and auth token
ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
ZAPIER_NLA_API_KEY = os.getenv('ZAPIER_NLA_API_KEY')

# OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Choose your model between gpt-3, gpt-3.5-turbo, gpt-4
SELECTED_MODEL = 'gpt-4'

# Temperature value for OpenAI language model
TEMPERATURE_VALUE = float(0.8)

# DALL-E settings
IMAGE_SIZE = "256x256"

# Chatbot name for generating responses
BOT_NAME = 'Lago'
