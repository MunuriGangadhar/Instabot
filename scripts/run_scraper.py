from src.scraper import scrape_instagram_profiles
from src.utils import setup_logging

if __name__ == "__main__":
    setup_logging()
    print("Starting Instagram Scraper...")
    scrape_instagram_profiles()
    print("Scraping completed.")
