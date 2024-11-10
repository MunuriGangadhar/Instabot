from instapy import InstaPy
import csv
from config.config import INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD

def send_automated_messages(input_file='data/instagram_data.csv'):
    session = InstaPy(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)
    session.login()
    
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            username = row['Username']
            message = f"Hi {row['Profile Name']}, I love your bakery content! Would love to collaborate!"
            
            try:
                session.send_message([username], message)
                print(f"Sent message to {username}")
            except Exception as e:
                print(f"Error sending message to {username}: {e}")
                continue

    session.end()
