

## 📂 Project Structure
```
instagram-bot/
├── config/
│   ├── config.py
│   └── .env
├── data/
│   └── instagram_data.csv
├── logs/
│   └── bot.log
├── scripts/
│   ├── run_bot.py
│   ├── run_scraper.py
│   └── run_messenger.py
├── src/
│   ├── __init__.py
│   ├── scraper.py
│   ├── messenger.py
│   ├── proxy_handler.py
│   └── utils.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/MunuriGangadhar/Instabot.git
cd instagram-bot
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# Activate the virtual environment
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🔧 Configuration

### 1. Set Up the `.env` File
Create a `.env` file in the `config/` directory with the following content:

```env
INSTAGRAM_USERNAME=your_instagram_username
INSTAGRAM_PASSWORD=your_instagram_password
SCRAPE_LIMIT=100
```

- Replace `your_instagram_username` and `your_instagram_password` with your Instagram login credentials.
- `SCRAPE_LIMIT` is the maximum number of accounts to scrape per keyword.

### 2. Update the Configuration (`config/config.py`)
Make sure the `config/config.py` file correctly loads the environment variables.

## 🚀 Usage

### 1. Run the Scraper
This script scrapes Instagram profiles based on predefined keywords.

```bash
python scripts/run_scraper.py
```
- Output will be saved to `data/instagram_data.csv`.

### 2. Run the Automated Messenger
This script sends personalized DMs to the scraped profiles.

```bash
python scripts/run_messenger.py
```

### 3. Run the Entire Bot (Scraper + Messenger)
To run the full bot (scraping + messaging in sequence):

```bash
python scripts/run_bot.py
```

### 4. Customize Keywords
You can customize the search keywords by modifying the `SCRAPE_KEYWORDS` list in `config/config.py`:

```python
SCRAPE_KEYWORDS = ["bakery", "cake", "cookies", "foodie", "chef", "desserts"]
```

## 📦 Dependencies

### Python Libraries
All the dependencies required for the project are listed in the `requirements.txt` file:

```
instaloader
dotenv
selenium
beautifulsoup4
pandas
requests
```

To install them, run:

```bash
pip install -r requirements.txt
```

### Required Tools
- [Python 3.8+](https://www.python.org/downloads/)
- [Google Chrome](https://www.google.com/chrome/) (for Selenium)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (Make sure to download the version that matches your Chrome browser)

### Installing ChromeDriver
Ensure that the `chromedriver` executable is in your system's PATH, or place it in the project root directory.

## 🛠️ Notes & Limitations
- Instagram has strict rate limits, so avoid running the bot for extended periods without breaks.
- Make sure to use proxies to avoid getting temporarily blocked by Instagram.
- The bot follows Instagram's policies, but excessive automation may still lead to account restrictions.
- Ensure that your Instagram account is not flagged as spam; start by messaging a small number of users initially.
  
## 🛡️ Proxy Support
To prevent being blocked by Instagram, update the list of proxies in `src/proxy_handler.py`:

```python
PROXIES = [
    'http://123.456.789.000:8080',
    'http://987.654.321.000:3128',
    'http://192.168.0.101:8000'
]
```

The bot randomly selects a proxy from this list during scraping.

## 🧪 Testing
To test individual modules:
- Run the scraper: `python scripts/run_scraper.py`
- Run the messenger: `python scripts/run_messenger.py`

