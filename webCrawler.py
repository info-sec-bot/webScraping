from bs4 import BeautifulSoup
import random
import re
import requests

# html = "https://en.wikipedia.org/wiki/Kevin_Bacon"

# Define the User-Agent header
# It's good practice to use a common browser's User-Agent string
# or a custom string that identifies your scraper.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
pages = set()
def getLinks(pageUrl):
    global pages
    html = "https://en.wikipedia.org" + pageUrl
    try:
        # Send a GET request to the URL with the specified headers
        response = requests.get(html, headers=headers)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Parse the HTML content using Beautiful Soup
        try:
            for link in soup.find_all('a', href=re.compile("^(/wiki/)")):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in pages:
                        # We have encountered a new page
                        newPage = link.attrs['href']
                        print(f"New page: {newPage}")
                        pages.add(newPage)
                        getLinks(newPage)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt detected. Exiting loop.")
            # Perform any cleanup or final actions here
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
getLinks("")