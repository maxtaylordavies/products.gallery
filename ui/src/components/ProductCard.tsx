import React from "react";
import { motion } from "framer-motion";

import "../App.css";
import Product from "../types/Product";

const ProductCard = (product: Product) => {
  return (
    <motion.div whileHover={{ scale: 1.1 }} whileTap={{ scale: 0.9 }}>
      <a href={product.url} className="product-card" target="_blank">
        <img src={product.image} height={200} width={200} />
      </a>
    </motion.div>
  );
};

export default ProductCard;
