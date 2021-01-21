import http
import json
import requests
import uuid

from bs4 import BeautifulSoup

from product import Product


def getHTML(url):
    page = requests.get(url)
    return BeautifulSoup(page.text, "html.parser")


def createID():
    return str(uuid.uuid4())


def toJSON(products, path):
    with open(path, "w") as f:
        json.dump([p.__dict__ for p in products], f)


def fromJSON(path):
    with open(path) as f:
        json_data = json.load(f)

    products = []
    for j in json_data:
        product = Product()
        product.fromDict(j)
        products.append(product)

    return products
