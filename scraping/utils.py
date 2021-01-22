import http
import json
import requests
import uuid

from bs4 import BeautifulSoup

from product import Product


def getHTML(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:69.0) Gecko/20100101 Firefox/69.0"
    }

    page = requests.get(url, headers=headers)
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
