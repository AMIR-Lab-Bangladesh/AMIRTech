import React from "react";
import logo from "../../assets/logo.png";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <div className="navbar-wrapper sticky">
      <div className="navbar bg-amirtech-dark text-white px-5 py-3 lg:mx  rounded-full">
        <div className="navbar-brand">
          <img src={logo} alt="logo" width={120} />
        </div>
        <div className="navbar-menu text-secondary ml-5">
          <li>
            <Link className="hover:text-white" to="/">
              Home
            </Link>
          </li>
          <li>
            <Link className="hover:text-white" to="/about">
              About
            </Link>
          </li>
          <li>
            <Link className="hover:text-white" to="/shop">
              Shop
            </Link>
          </li>
          <li>
            <Link className="hover:text-white" to="/contact">
              Contact
            </Link>
          </li>
        </div>
      </div>
    </div>
  );
};

export default Navbar;
