import time

from product import Product
from utils import getHTML, createID, toJSON, fromJSON


def getAll(logfn):
    allProducts = []
    page = 1

    while True:
        pageOfProducts = getPageOfProducts(page, logfn)

        if len(pageOfProducts) == 0:
            break

        allProducts += pageOfProducts
        page += 1

    return allProducts


def getPageOfProducts(pageNum, logfn):
    time.sleep(0.5)
    products = []
    base = "https://www.ica.art"

    url = f"{base}/bookstore?type=All&page={pageNum}"
    logfn(url)
    soup = getHTML(url)

    items = soup.find_all(class_="item merchandise")
    for item in items:
        link = item.a
        products.append(
            Product(createID(), f"{base}{link['href']}", link.find_all("div")[2].img["src"]))

    return products
