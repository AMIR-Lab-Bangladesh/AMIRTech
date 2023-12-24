import React from "react";
import Layout from "../components/Layout";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import API_URL from "../config";

const Login = () => {
  let navigate = useNavigate();
  const client = axios.create({
    baseURL: `${API_URL}`,
  });

  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");

  function handleLogin(e) {
    e.preventDefault();
    console.log(email, password);
    // prettier-ignore
    client
      .post("/auth/token/jwt/create", {
        email: email,
        password: password
      })
      .then(function (res) {
        // setCurrentUser(true);
        navigate("/");
      });
  }

  console.log(API_URL);
  return (
    <Layout>
      <div className="sm:mx-3">
        <h1 className="text-3xl font-bold">Login</h1>

        <form className="mt-3" onSubmit={(e) => handleLogin(e)}>
          <div className="mb-5">
            <input onChange={(e) => setEmail(e.target.value)} type="email" name="email" id="email" placeholder="Enter Email" className="w-full px-3 py-3 mb-3 placeholder-gray-300 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-transparent" />

            <input onChange={(e) => setPassword(e.target.value)} type="password" name="password" id="password" placeholder="Enter Password" className="w-full px-3 py-3 placeholder-gray-300 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-transparent" />

            <button type="submit" className="w-full px-3 py-4 mt-3 text-white bg-purple rounded-md focus:bg-blue-500 focus:outline-none">
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
