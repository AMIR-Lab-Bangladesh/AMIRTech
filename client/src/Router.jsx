import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import App from "./App";

const Router = () => {
  return (
    <BrowserRouter basename="/">
      <Routes>
        <Route exact path="" element={<App />} />
        {/* <Route exact path="/articles" element={<Articles />} />
        <Route exact path="/article/:link" element={<Article />} /> */}
      </Routes>
    </BrowserRouter>
  );
};

export default Router;
