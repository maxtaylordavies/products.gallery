import json
import time

from product import Product
from utils import getHTML, createID, toJSON, fromJSON


def getAll(logfn):
    allProducts = []
    productTypes = [
        "art-posters",
        "epic-posters",
        "mini-posters",
        "art-postcards",
        "artists-books",
        "art-reference-books",
        "address-books",
        "calendars-diaries",
        "keyrings",
        "mens-accessories",
        "pocket-mirrors",
        "tshirts",
        "walking-sticks",
        "fridge-magnets",
        "frames",
        "tableware",
        "tea-towels",
        "collectibles",
        "activity-books-for-kids",
        "craft-play",
        "educational",
        "games-puzzles",
        "story-books",
        "toys",
        "hobbies-and-crafts"
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

    base = "https://www.nationalgallery.co.uk"
    url = f"{base}/products/{productType}?orderBy=&VIEW_SIZE=100&VIEW_INDEX={pageNum}"

    logfn(url)
    soup = getHTML(url)

    items = soup.find_all(class_="productwrap")
    for item in items:
        products.append(
            Product(createID(), f"{base}{item.a['href']}", f"{base}{item.a.div.img['src']}"))

    return products
