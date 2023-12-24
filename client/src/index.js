import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
// import App from "./App";
import Router from "./Router";
import API_URL from "./config";


export const axiosInstance = axios.create({
  baseURL: API_URL,
  timeout: 5000,
  headers: {
    "Content-Type": "application/json",
    accept: "application/json",
  },
});
axiosInstance.interceptors.request.use(
  config => {
    const token = "JWT " + localStorage.getItem("access");
    if (token) {
      config.headers.authorization = token;
    }
    return config;
    
  },
 err =>  {
    console.log(err);
    // console.log('hello')
    return Promise.reject(err);
  }

);


const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <Router />
  </React.StrictMode>
);
