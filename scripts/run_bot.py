from src.schedule import schedule_bot
from src.utils import setup_logging

if __name__ == "__main__":
    setup_logging()
    print("Starting Instagram Bot...")
    schedule_bot()
