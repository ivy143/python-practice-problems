# URL shortener
import requests
import string
import random
def shorten_url(long_url):
    api_url = "https://api.shrtco.de/v2/shorten?url=" + long_url
    response = requests.get(api_url)
    if response.status_code == 201 or response.status_code == 200:
        data = response.json()
        return data['result']['short_link']
    else:
        return None
# Example usage
long_url = "https://www.example.com/some/very/long/url"
short_url = shorten_url(long_url)
if short_url:
    print("Shortened URL:", short_url)
else:
    print("Failed to shorten the URL.")
# Note: This code uses the shrtco.de URL shortening service API. Make sure to check their usage policy and limits before using it extensively.