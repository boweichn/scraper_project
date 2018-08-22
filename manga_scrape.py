from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = "http://www.crunchyroll.com/videos/anime/updated"

# opening up connection and grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
# closes the client
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each products. (finds all divs thats a class of "item-container")
containers = page_soup.findAll("div", {"class":"NRoaY"})