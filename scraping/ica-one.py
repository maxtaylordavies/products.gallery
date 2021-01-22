from product import Product
from utils import getHTML, createID, toJSON, fromJSON


def main():
    allProducts = fromJSON("./products.json")
    lengthThen = len(allProducts)

    page = 1
    while True:
        pageOfProducts = getPageOfProducts(page)

        if len(pageOfProducts) == 0:
            break

        for p in pageOfProducts:
            if not p.isIn(allProducts):
                allProducts.append(p)

        page += 1

    lengthNow = len(allProducts)
    print(f"Done! Scraped {lengthNow - lengthThen} new products!")
    toJSON(allProducts, "products.json")


def getPageOfProducts(pageNum):
    products = []

    url = f"https://ica-bookstore.myshopify.com/collections/frontpage?page={pageNum}"
    print(url)
    soup = getHTML(url)

    items = soup.find_all(class_="grid-view-item")
    for item in items:
        products.append(
            Product(createID(), item.a["href"], item.div.img["src"]))

    return products


if __name__ == "__main__":
    main()
