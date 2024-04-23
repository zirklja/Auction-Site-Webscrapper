import requests
from bs4 import BeautifulSoup

URL = "https://www.propertyroom.com/c/propertyroom/1"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


def locate_price_time():
    pricentime = soup.find_all("div", class_="time-bids-category")
    for i in range(0, len(pricentime), 2):
        sold_item = 'Closed'

        if i == sold_item:
            pass
        else:
            item_pair1 = pricentime[i].text.strip()
            item_pair2 = item_pair1.split('\n')
            time_left = item_pair2[0]
            price = item_pair2[1]
            return time_left and price


def item_name():
    product_div = soup.find("div", class_="product-name-category")
    for each in product_div:
        name = [a.text.strip() for a in product_div.find_all("a")]

    print(name)

locate_price_time()

# locate_price_time()


# Below is to find a Class element
# soup.find_all("div"<- this is the element name, class_="")
# Below is to find a id element
# soup.find(id="")
