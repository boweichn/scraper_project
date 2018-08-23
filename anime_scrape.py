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
containers = page_soup.findAll("div", {"class":"wrapper hover-toggle-queue container-shadow hover-classes"})

def anime_parser():
    anime_list = []
    for container in containers:

        # finding the title of the anime
        title = container.a["title"]

        # finding the most recent episode number
        episode_container = container.find("span", {"class", "series-data block ellipsis"})
        recent_episode = episode_container.text.strip()

        # finding thumbnail of the dom element
        thumb_container = container.find("img", {"class", "portrait"})
        thumb_src = thumb_container["src"]

        combined_item = [title, recent_episode, thumb_src]
        anime_list.append(', '.join(combined_item))
    return anime_list


# episode_container = containers[0].find("span", {"class", "series-data block ellipsis"})
# recent_episode = episode_container.text.strip()
# print(recent_episode)

if __name__ == "__main__":
    for items in anime_parser():
        print(items)