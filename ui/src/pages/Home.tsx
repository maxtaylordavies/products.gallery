import React, { useState, useEffect, useRef } from "react";
import axios from "axios";

import Header from "../components/Header";
import ProductCard from "../components/ProductCard";
import Product from "../types/Product";
import "../App.css";

const Home = () => {
  const [loading, setLoading] = useState(true);
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
      <div
        className="product-grid"
        onScroll={() => {
          onScroll();
        }}
        ref={gridRef}
      >
        {products.map(ProductCard)}
      </div>
    </>
  );
};

export default Home;
