import schedule
import time
from src.scraper import scrape_instagram_profiles
from src.messenger import send_automated_messages

def schedule_bot():
    # Schedule scraping once a week and messaging daily
    schedule.every().week.do(scrape_instagram_profiles)
    schedule.every().day.at("10:00").do(send_automated_messages)

    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    schedule_bot()
