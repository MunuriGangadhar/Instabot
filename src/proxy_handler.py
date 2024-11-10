import random

# Example list of proxy servers
PROXIES = [
    'http://123.456.789.000:8080',
    'http://987.654.321.000:3128',
    'http://192.168.0.101:8000'
]

def get_random_proxy():
    return random.choice(PROXIES)
