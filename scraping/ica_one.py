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
    base = "https://ica-bookstore.myshopify.com"

    url = f"{base}/collections/frontpage?page={pageNum}"
    logfn(url)
    soup = getHTML(url)

    items = soup.find_all(class_="grid-view-item")
    for item in items:
        products.append(
            Product(createID(), f"{base}{item.a['href']}", f"https:{item.div.img['src']}"))

    return products
