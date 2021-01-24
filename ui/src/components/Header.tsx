import React from "react";
import "../App.css";

const Header = () => {
  return (
    <header>
      <a href="/" className="home-link">
        products.gallery
      </a>
      <a href="/about" className="about-link">
        about
      </a>
    </header>
  );
};

export default Header;
