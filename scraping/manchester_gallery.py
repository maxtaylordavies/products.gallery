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
    base = "https://shop.manchesterartgallery.org"

    url = f"{base}/collections/all?page={pageNum}"
    logfn(url)
    soup = getHTML(url)

    items = soup.find_all(class_="product-card")
    for item in items:
        products.append(
            Product(createID(), f"{base}{item.a['href']}", f"https:{item.div.div.div.img['data-src']}".replace(r"{width}", "200")))

    return products
