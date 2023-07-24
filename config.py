from dotenv import load_dotenv
import os

load_dotenv()

# bot connect information
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# database connect information
USER = os.environ.get("USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")