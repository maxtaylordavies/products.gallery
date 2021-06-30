from utils import fromJSON, toJSON
from tate import getAll as getAllTate
from ica_one import getAll as getAllICAOne

# from ica_two import getAll as getAllICATwo
from design_museum import getAll as getAllDesignMuseum
from national_gallery import getAll as getAllNationalGallery
from ra import getAll as getAllRA
from manchester_gallery import getAll as getAllManchester
from nottingham_contemporary import getAll as getAllNottingham
from southbank import getAll as getAllSouthbank
from slg import getAll as getAllSLG
from camden_arts import getAll as getAllCamdenArts


def main():
    allProducts = []

    fns = [
        getAllTate,
        getAllICAOne,
        # getAllICATwo,
        getAllDesignMuseum,
        getAllNationalGallery,
        getAllRA,
        getAllManchester,
        getAllNottingham,
        getAllSouthbank,
        getAllSLG,
        getAllCamdenArts,
    ]

    for fn in fns:
        products = fn(print)
        for p in products:
            if not p.isIn(allProducts):
                allProducts.append(p)

    print(f"Done! Scraped {len(allProducts)} products!")
    toJSON(allProducts, "products.json")


if __name__ == "__main__":
    main()
