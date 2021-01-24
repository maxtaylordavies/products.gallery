import json
import time

from product import Product
from utils import getHTML, createID, toJSON, fromJSON


def getAll(logfn):
    allProducts = []
    productTypes = [
        "collections/shop-contemporary",
        "collections/limited-editions",
        "collections/publications"
    ]

    for pt in productTypes:
        products = getAllProductsOfType(pt, logfn)
        allProducts += products

    return allProducts


def getAllProductsOfType(productType, logfn):
    products = []

    base = "https://nottinghamcontemporary.shop"
    url = f"{base}/{productType}"
    logfn(url)

    soup = getHTML(url)

    items = soup.find_all(class_="Item--product")
    for item in items:
        products.append(
            Product(createID(), f"{base}{item.a['href']}", f"https:{extractImageUrlFromStyle(item.a.div.div.div['style'])}"))

    return products


def extractImageUrlFromStyle(style):
    return style.split(" ")[1][4:-1]
