import React from "react";
import Layout from "../components/Layout";

import API_URL from "../config";

const Login = () => {
  console.log(API_URL);
  return (
    <Layout>
      <div className="mx-10">
        <h1 className="text-3xl font-bold">Login</h1>
        <p className="text-xl">Login to your account</p>

        <form className="mt-10">
          <div className="mb-5">
            <input
              type="email"
              name="email"
              id="email"
              placeholder="
                Enter Email"
              className="w-full px-3 py-2 mb-3 placeholder-gray-300 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-transparent"
            />

            <input type="password" name="password" id="password" placeholder="Enter Password" className="w-full px-3 py-2 placeholder-gray-300 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-transparent" />

            <button type="submit" className="w-full px-3 py-4 mt-5 text-white bg-purple rounded-md focus:bg-blue-500 focus:outline-none">
              Login
            </button>

            <p className="mt-5 text-sm text-gray-600 dark:text-gray-400">
              Don't have an account?{" "}
              <a href="#" className="text-blue-500 focus:outline-none focus:underline focus:text-blue-400">
                Register
              </a>
            </p>
          </div>
        </form>
      </div>
    </Layout>
  );
};

export default Login;
