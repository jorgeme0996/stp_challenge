from dotenv import load_dotenv
import os

load_dotenv()

VIRUS_TOTAL_API_KEY = os.getenv("VIRUS_TOTAL_API_KEY")
