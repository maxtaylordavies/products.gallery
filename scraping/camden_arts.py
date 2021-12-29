import time

from product import Product
from utils import getHTML, createID


def getAll(logfn):
    allProducts = []
    productTypes = [
        "artists-editions",
        "camden-publications",
        "exhibition-related",
        "ceramics",
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


def getPageOfProducts(productType, page, logfn):
    time.sleep(0.5)
    products = []

    base = "https://shop.camdenartscentre.org"
    url = f"{base}/collections/{productType}?page={page}"
    logfn(url)

    soup = getHTML(url)
    tiles = soup.find_all(class_="product-card")

    for tile in tiles:
        img = tile.find(class_="grid-view-item__image")
        widths = img["data-widths"]  # e.g. '[180, 360, 540, 720]'
        width = widths[1:-1].split(",")[0]  # e.g. '180'
        img_url = f"https:{img['data-src'].replace('{width}', width)}"

        products.append(Product(createID(), f'{base}{tile.a["href"]}', img_url))

    return products
