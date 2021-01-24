import React from "react";

import Header from "../components/Header";
import "../App.css";

const galleries: { [key: string]: string } = {
  barbican: "https://www.barbican.org.uk/",
  dm: "https://designmuseum.org/",
  ica: "https://www.ica.art/",
  manchester: "https://manchesterartgallery.org/",
  national_gallery: "https://www.nationalgallery.co.uk/",
  nottingham: "https://www.nottinghamcontemporary.org/",
  ra: "https://www.royalacademy.org.uk/",
  southbank: "https://www.southbankcentre.co.uk/",
  tate: "https://www.tate.org.uk/",
};

const About = () => {
  return (
    <>
      <Header />
      <div className="about-page">
        <span className="about-text">
          products.gallery is a storefront for showcasing products sold by many
          different UK art galleries. <a href="https://maxtaylordavi.es">i</a>{" "}
          built it because i like browsing these stores as a form of
          procrastination, and i thought it would be cool to have a single space
          collecting all of their interesting wares. you can view the code{" "}
          <a href="https://www.github.com/maxtaylordavies/products.gallery">
            here
          </a>
        </span>
        <div className="logos">
          {Object.keys(galleries).map((k: string) => {
            <a href={galleries[k]} target="_blank">
              <img src={`../logos/${k}.png`} />
            </a>;
          })}
        </div>
      </div>
    </>
  );
};

export default About;
