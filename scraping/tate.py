import json
import time

from product import Product
from utils import getHTML, createID, toJSON, fromJSON


def getAll(logfn):
    allProducts = []
    productTypes = ["prints", "books", "fashion", "home"]

    for pt in productTypes:
        products = getAllProductsOfType(pt, logfn)
        allProducts += products

    return allProducts


def getAllProductsOfType(productType, logfn):
    products = []
    page = 1
    while True:
        pageOfProducts = getPageOfProducts(productType, page, logfn)

        if len(pageOfProducts) == 0:
            break

        products += pageOfProducts
        page += 1

    return products


def getPageOfProducts(productType, pageNum, logfn):
    time.sleep(0.5)
    products = []
    base = "https://shop.tate.org.uk"

    url = f"{base}/{productType}/view-all-{productType}?start={(pageNum - 1) * 100}&sz=100"
    logfn(url)
    soup = getHTML(url)

    tiles = soup.find_all(class_="product-tile")
    for tile in tiles:
        products.append(
            Product(createID(), f"{base}{tile.div.a['href']}", tile.div.img["src"]))

    return products
