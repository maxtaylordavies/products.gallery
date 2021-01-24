import time

from product import Product
from utils import getHTML, createID, toJSON, fromJSON


def getAll(logfn):
    allProducts = []
    productTypes = [
        "collections/hayward-gallery",
        "collections/print-shop",
        "collections/homeware",
        "collections/books",
        "collections/jewellery-accessories",
        "collections/lifestyle",
        "collections/festivals",
        "collections/gifts"
    ]

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

    base = "https://shop.southbankcentre.co.uk"
    url = f"{base}/{productType}?page={pageNum}"

    logfn(url)
    soup = getHTML(url)

    items = soup.find_all("a", class_="grid__image")
    for item in items:
        products.append(
            Product(createID(), f"{base}{item['href']}", f"https:{item.img['src']}"))

    return products
