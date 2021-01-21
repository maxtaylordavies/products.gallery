import json
import time

from product import Product
from utils import getHTML, createID, toJSON, fromJSON


def main():
    productTypes = ["prints", "books", "fashion", "home"]

    allProducts = fromJSON("./products.json")
    lengthThen = len(allProducts)

    for pt in productTypes:
        products = getAllProductsOfType(pt)
        for p in products:
            if not p.isIn(allProducts):
                allProducts.append(p)

    lengthNow = len(allProducts)
    print(f"Done! Scraped {lengthNow - lengthThen} new products!")
    toJSON(allProducts, "products.json")


def getAllProductsOfType(productType):
    products = []
    page = 1
    while True:
        pageOfProducts = getPageOfProducts(productType, page)

        if len(pageOfProducts) == 0:
            break

        products += pageOfProducts
        page += 1

    return products


def getPageOfProducts(productType, pageNum):
    time.sleep(0.2)

    products = []

    url = f"https://shop.tate.org.uk/{productType}/view-all-{productType}?start={(pageNum - 1) * 100}&sz=100"
    soup = getHTML(url)

    tiles = soup.find_all(class_="product-tile")
    for tile in tiles:
        products.append(
            Product(createID(), tile.div.a["href"], tile.div.img["src"]))

    return products


if __name__ == "__main__":
    main()
