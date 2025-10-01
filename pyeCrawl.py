from bs4 import BeautifulSoup
from urllib.parse import urlparse
import random
import re
import requests

# Retrieves a list of all Internal links found on a page
def getInternalLinks(soup, includeUrl):
    internalLinks = []
    # Finds all links that begin with a "/"
    for link in soup.find_all('a', href=re.compile("^(/|.*(http://"+includeUrl+")).*")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

# Retrieves a list of all external links found on a page
def getExternalLinks(soup, includeUrl):
    excludeUrl = getDomain(url)
    externalLinks = []
    # Finds all links that start with http or www that don't contain the parent url
    for link in soup.find_all('a', href=re.compile("^(http)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None and len(link.attrs['href']) != 0:
            externalLinks.append(link.attrs['href'])
    return externalLinks

def getDomain(address):
    return urlparse(address).netloc
url = "https://en.wikipedia.org/wiki/Kevin_Bacon"

# Define the User-Agent header
# It's good practice to use a common browser's User-Agent string
# or a custom string that identifies your scraper.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
try:
    # Send a GET request to the URL with the specified headers
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')
    for item in getInternalLinks(soup, url):
        print(item)
    print(type(getInternalLinks(soup, url)))
    for item in getExternalLinks(soup, url):
        print(item)

    print(type(getInternalLinks(soup, url)))
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")