from product import Product
from utils import getHTML, createID


def getAll(logfn):
    allProducts = []
    productTypes = [
        "artist-editions",
        "artist-monographs",
        "slg-gifts",
        "slg-publications",
    ]

    for pt in productTypes:
        products = getAllProductsOfType(pt, logfn)
        allProducts += products

    return allProducts


def getAllProductsOfType(productType, logfn):
    url = f"https://www.southlondongallery.org/product-tag/{productType}/"
    logfn(url)
    soup = getHTML(url)

    tiles = soup.find_all(class_="tease-product")
    return [
        Product(createID(), tile.a["href"], tile.a.div.img["src"]) for tile in tiles
    ]
