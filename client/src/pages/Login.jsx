import React, { useEffect, useState } from "react";
import useForm from "../hooks/useForm";
import { useDispatch, useSelector } from "react-redux";
import Layout from "../components/Layout";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import API_URL from "../config";
import { login } from "../redux/asyncActions/UserAsync";
import ClipLoader from "react-spinners/ClipLoader";

const Login = () => {
  const user = useSelector((state) => state.userReducer);
  const { isAuthenticated } = false; //user;
  const [values, handleChange] = useForm();
  const [type, setType] = useState("password");
  const { email, password, username } = values;
  const dispatch = useDispatch();
  const history = useNavigate();
  useEffect(() => {
    isAuthenticated && history.push("/");
  }, [history, isAuthenticated]);

  const loginMe = (e) => {
    e.preventDefault();
    dispatch(login(email, password));
  };
  // const changetype = () => {
  //   if (type === "password") {
  //     setType("text");
  //   }
  //   if (type === "text") {
  //     setType("password");
  //   }
  // };
  // user = userSelector((state) => state.user);
  // let navigate = useNavigate();
  // const client = axios.create({
  //   baseURL: `${API_URL}`,
  // });

  // const [email, setEmail] = React.useState("");
  // const [password, setPassword] = React.useState("");

  // function handleLogin(e) {
  //   e.preventDefault();
  //   console.log(email, password);
  //   // prettier-ignore
  //   client
  //     .post("/auth/token/jwt/create/", {
  //       email: email,
  //       password: password
  //     })
  //     .then(function (res) {
  //       // setCurrentUser(true);
  //       navigate("/");
  //     });
  // }

  // console.log(API_URL);
  return (
    <Layout>
      <div className="sm:mx-3">
        <h1 className="text-3xl font-bold">Login</h1>

        <form className="mt-3" onSubmit={loginMe}>
          <div className="mb-5">
            <input
              value={email || ""}
              onChange={handleChange}
              type="email"
              name="email"
              id="email"
              placeholder="Enter Email"
              className="w-full px-3 py-3 mb-3 placeholder-gray-300 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-transparent"
            />

            <input
              value={password || ""}
              onChange={handleChange}
              type="password"
              name="password"
              id="password"
              placeholder="Enter Password"
              className="w-full px-3 py-3 placeholder-gray-300 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-transparent"
            />
            <button
              type="submit"
              disabled={!email || !password}
              className="w-full px-3 py-4 mt-3 text-white bg-purple rounded-md focus:bg-blue-500 focus:outline-none"
            >
              {user.isLoading ? (
                <ClipLoader color="white" loading={true} size={26} />
              ) : (
                "Login"
              )}
            </button>

            {/* <button
              type="submit"
              className="w-full px-3 py-4 mt-3 text-white bg-purple rounded-md focus:bg-blue-500 focus:outline-none"
            >
              Login
            </button> */}

            <p className="mt-5 text-sm text-gray-600 dark:text-gray-400">
              Don't have an account?{" "}
              <a
                href="#"
                className="text-blue-500 focus:outline-none focus:underline focus:text-blue-400"
              >
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
