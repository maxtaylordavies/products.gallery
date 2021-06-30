import React from "react";
import { motion } from "framer-motion";
import "../App.css";

const Header = () => {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="header"
    >
      <motion.div whileHover={{ scale: 1.03 }} whileTap={{ scale: 0.95 }}>
        <a href="/" className="home-link">
          products.galleryyyyyy
        </a>
      </motion.div>
      <a href="/about" className="about-link">
        about
      </a>
    </motion.div>
  );
};

export default Header;
