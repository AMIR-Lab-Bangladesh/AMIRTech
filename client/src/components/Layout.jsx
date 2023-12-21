import React from "react";
import Navbar from "./base/Navbar";
import Footer from "./base/Footer";

const Layout = ({ children }) => {
  return (
    <div>
      <Navbar />
      <div className="mt-4 mb-4">{children}</div>
      <Footer />
    </div>
  );
};

export default Layout;
