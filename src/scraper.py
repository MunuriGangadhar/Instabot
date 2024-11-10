import instaloader
import csv
import os
from config.config import INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD, SCRAPE_KEYWORDS
from src.proxy_handler import get_random_proxy
from src.utils import log_message

def scrape_instagram_profiles(output_file='data/instagram_data.csv'):
    L = instaloader.Instaloader()

    # Login with Instagram credentials
    try:
        L.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
    except Exception as e:
        log_message(f"Error logging in: {e}")
        return

    os.makedirs('data', exist_ok=True)
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Profile Name', 'Username', 'Bio', 'Follower Count', 'Engagement Rate', 'Recent Posts', 'Email'])

        for keyword in SCRAPE_KEYWORDS:
            log_message(f"Searching for accounts using keyword: {keyword}")
            for post in instaloader.Hashtag.from_name(L.context, keyword).get_posts():
                username = post.owner_username

                try:
                    L.context.session.proxies = {"http": get_random_proxy(), "https": get_random_proxy()}
                    profile_data = instaloader.Profile.from_username(L.context, username)
                    bio = profile_data.biography
                    posts = [post.url for post in profile_data.get_posts()[:3]]  # Latest 3 posts

                    writer.writerow([
                        profile_data.full_name,
                        username,
                        bio,
                        profile_data.followers,
                        f"{profile_data.followers / profile_data.followees:.2f}" if profile_data.followees else 'N/A',
                        posts,
                        profile_data.business_email,
                    ])
                    log_message(f"Profile scraped: {username}")

                except Exception as e:
                    log_message(f"Error fetching data for {username}: {e}")
                    continue

    log_message(f"Data scraping completed. Saved to {output_file}.")
