import time

from product import Product
from utils import getHTML, createID


def getAll(logfn):
    allProducts = []
    productTypes = [
        "artist-editions",
        "camden-publications",
        "exhibition-related",
        "recommended",
        "childrens-books-stationary",
    ]

    for pt in productTypes:
        products = getAllProductsOfType(pt, logfn)
        allProducts += products

    return allProducts


def getAllProductsOfType(productType, logfn):
    products = []
    page = 0
    while True:
        pageOfProducts = getPageOfProducts(productType, page, logfn)

        if pageOfProducts[0].isIn(products):
            break

        products += pageOfProducts
        page += 21

    return products


def getPageOfProducts(productType, page, logfn):
    time.sleep(0.5)
    products = []

    base = "https://shop.camdenartscentre.org"
    url = f"{base}/shop/c/{productType}/P{page}"
    logfn(url)

    soup = getHTML(url)
    tiles = soup.find_all(class_="shop-item-image")

    for tile in tiles:
        a = tile.find("a")
        products.append(
            Product(createID(), f'{base}{a["href"]}', f'{base}{a.img["src"]}')
        )

    return products
