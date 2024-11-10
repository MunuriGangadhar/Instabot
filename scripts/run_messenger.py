from src.messenger import send_automated_messages
from src.utils import setup_logging

if __name__ == "__main__":
    setup_logging()
    print("Starting Instagram Messenger...")
    send_automated_messages()
    print("Messaging completed.")
