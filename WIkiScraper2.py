from bs4 import BeautifulSoup
import random
import re
import requests

url = "https://en.wikipedia.org/wiki/Kevin_Bacon"

# Define the User-Agent header
# It's good practice to use a common browser's User-Agent string
# or a custom string that identifies your scraper.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
random.seed()
def getLinks(articleUrl):

    try:
        # Send a GET request to the URL with the specified headers
        response = requests.get(articleUrl, headers=headers)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find('div', attrs={'id':"bodyContent"}).find_all('a', href=re.compile("^(/wiki/)((?!:).)*$"))
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
# print(getLinks(url))
# Get a list of links from url
try:
    links = getLinks(url)
    print("Press 'q' to quit")
    while len(links) > 0:
        # Choose random link from page
        newArticle = links[random.randint(0,len(links)-1)].attrs['href']
        print(newArticle)
        #Create new link continue looping
        links = getLinks(f"https://en.wikipedia.org{newArticle}")
except KeyboardInterrupt:
    print("\nKeyboardInterrupt detected. Exiting loop.")
    # Perform any cleanup or final actions here
