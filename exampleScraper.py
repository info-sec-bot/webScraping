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
# DeprecationWarning: The 'text' argument to find()-type methods is deprecated. Use 'string' instead.
namelist = bsObj.find_all(string="King of Prussia")
for name in namelist:
    print(f"***The string occurs {len(namelist)} in the html***")
# Return all span tags with the class attribute red
allText = bsObj.find_all("span",class_="red")
for text in allText:
    print(text.get_text())
# Find all header tags
allhTags = bsObj.find_all({"h1", "h2"})
i = 1
for text in allhTags:
    print(f"This is the h{i} tag {text.get_text()}")
    i += 1
