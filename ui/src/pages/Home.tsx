import React, { useState, useEffect, useRef } from "react";
import { motion } from "framer-motion";
import axios from "axios";

import Header from "../components/Header";
import ProductCard from "../components/ProductCard";
import Product from "../types/Product";
import "../App.css";

const Home = () => {
  const [products, setProducts] = useState<Product[]>([]);
  const gridRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    fetchProducts(20);
  }, []);

  const fetchProducts = (n: number) => {
    axios.get(`${window.location.origin}/products?n=${n}`).then((resp: any) => {
      setProducts(products.concat(resp.data));
    });
  };

  const onScroll = () => {
    if (gridRef.current) {
      const { scrollTop, scrollHeight, clientHeight } = gridRef.current;
      if (scrollTop + clientHeight === scrollHeight) {
        fetchProducts(20);
      }
    }
  };

  return (
    <>
      <Header />
      <motion.div
        className="product-grid"
        onScroll={() => {
          onScroll();
        }}
        ref={gridRef}
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
      >
        {products.map(ProductCard)}
      </motion.div>
    </>
  );
};

export default Home;
