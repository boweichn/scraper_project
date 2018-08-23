from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup as soup

# opening up connection and grabbing the page
my_url = "https://mangarock.com"
uClient = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
page_html = uReq(uClient).read()

# closes the client
uReq(uClient).close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each products. (finds all divs thats a class of "item-container")
containers = page_soup.findAll("div", {"class":"NRoaY"})

def manga_parser():
    manga_list = []
    for container in containers:

        # finding the title of the manga
        title = container.div.meta["content"]

        # finding the most recent episode number
        chapter_container = container.find("a", {"class", "_2dU-m Mq7mR"})
        recent_chapter = chapter_container.text.strip()

        # finding thumbnail of the dom element
        thumb_container = container.find("meta", itemprop="image")
        thumb_src = thumb_container["content"]

        # find the hyperlink of the latest chapter
        hyperlink_container = container.find("a", {"class", "_2dU-m Mq7mR"})
        recent_chapter_hyperlink = "https://mangarock.com" + hyperlink_container["href"]

        combined_item = [title, recent_chapter, recent_chapter_hyperlink, thumb_src]
        manga_list.append(', '.join(combined_item))
    return manga_list

def main():
    for item in manga_parser():
        print(item)
    return

if __name__ == "__main__":
    main()
