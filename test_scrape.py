from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = "https://www.newegg.ca/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"

# opening up connection and grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
# closes the client
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each products. (finds all divs thats a class of "item-container")
containers = page_soup.findAll("div", {"class":"item-container"})

def sale_parser():
    for container in containers:

        # finding brand name
        brand = container.div.div.a.img["title"]

        # finding the product name
        title_container = container.findAll("a", {"class", "item-title"})
        product_name = title_container[0].text

        # finding the shipping price
        shipping_container = container.findAll("li", {"class", "price-ship"})
        shipping_price = shipping_container[0].text.strip()

        # finding the product price
        title_container = container.findAll("li", {"class", "price-current"})
        product_price = "$" + title_container[0].strong.text + title_container[0].sup.text

        sales_list = [brand, product_name, shipping_price, product_price]
        print(sales_list)
    return 

def testing_dot_divs():
    contain = containers[0]
    print(contain.div.div.a.img["title"])
    return

def testing_findAll():
    contain = containers[0]
    title_container = contain.findAll("a", {"class", "item-title"})
    print(title_container[0].text)
    return 

def testing_shipping():
    contain = containers[0]
    shipping_container = contain.findAll("li", {"class", "price-ship"})
    print(shipping_container[0].text.strip())
    return 

def testing_price():
    contain = containers[0]
    title_container = contain.findAll("li", {"class", "price-current"})
    print(title_container[0].strong.text + title_container[0].sup.text)
    return 

def main():
    sale_parser()
    return

if __name__ == "__main__":
    main()