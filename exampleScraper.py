from urllib.request import urlopen
from bs4 import BeautifulSoup
# Create HTML document
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# Build BeautifulSoup object - book update html.parser feature
bsObj = BeautifulSoup(html, "html.parser")
print(bsObj.prettify())

# Use find_all() - book update *findAll() deprecated* - to extract a Python list of proper nouns found by selecting <span class="green"> tags
namelist = bsObj.find_all("span", {"class": "green"})
for name in namelist:
    print(name.get_text())
