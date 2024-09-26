import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
TODOIST_API_TOKEN = os.getenv("TODOIST_API_TOKEN")
