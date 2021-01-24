import React from "react";

import "../App.css";

import Product from "../types/Product";

const ProductCard = (product: Product) => {
  return (
    <a href={product.url} className="product-card" target="_blank">
      <img src={product.image} height={200} width={200} />
    </a>
  );
};

export default ProductCard;
