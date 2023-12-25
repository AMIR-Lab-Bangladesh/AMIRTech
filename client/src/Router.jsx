import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import App from "./App";
import About from "./pages/About";
import Login from "./pages/Login";

const Router = () => {
  return (
    <BrowserRouter basename="/">
      <Routes>
        <Route exact path="" element={<App />} />
        <Route exact path="/about" element={<About />} />
        <Route exact path="/login" element={<Login />} />
        {/* <Route exact path="/articles" element={<Articles />} />
        <Route exact path="/article/:link" element={<Article />} /> */}
      </Routes>
    </BrowserRouter>
  );
};

export default Router;
