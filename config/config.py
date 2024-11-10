import os
from dotenv import load_dotenv


load_dotenv()

INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

if not INSTAGRAM_USERNAME or not INSTAGRAM_PASSWORD:
    raise ValueError("Please set your Instagram credentials in the .env file.")

SCRAPE_KEYWORDS = ["bakery", "cake", "cookies", "foodie", "chef", "desserts"]
SCRAPE_LIMIT = int(os.getenv("SCRAPE_LIMIT", 50))  # Default to 50 if not specified
