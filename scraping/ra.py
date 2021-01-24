import json
import time

from product import Product
from utils import getHTML, createID, toJSON, fromJSON


def getAll(logfn):
    allProducts = []
    productTypes = [
        "art-artists/all-artworks",
        "reproductions/posters-prints",
        "art-material/all-art-materials",
        "books/bookshop",
        "fashion/jewellery",
        "bags",
        "scarves",
        "kids",
        "lifestyle/life/homeware",
        "lifestyle/life/entertaining"
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

        if pageOfProducts[0].isIn(products):
            break

        products += pageOfProducts
        page += 1

    return products


def getPageOfProducts(productType, pageNum, logfn):
    time.sleep(0.5)
    products = []

    base = "https://shop.royalacademy.org.uk"
    url = f"{base}/{productType}?p={pageNum}"

    logfn(url)
    soup = getHTML(url)

    items = soup.find_all(class_="product-item-photo")
    for item in items:
        products.append(
            Product(createID(), item['href'], item.span.span.img['data-src']))

    return products
