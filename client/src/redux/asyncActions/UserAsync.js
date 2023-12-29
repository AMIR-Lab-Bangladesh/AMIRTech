import { setLoading, loginSuccess, refreshSuccess, userSuccess, profileUserSuccess, removeMessage, userRegisterSuccess, userFail, authSuccess, setMeta, logMeOut } from "../slices/UserSlice.js";

import axios from "axios";
import { axiosInstance } from "../../index";
import API_URL from "../../config.jsx";

export const load_user = () => async (dispatch) => {
  if (localStorage.getItem("access")) {
    try {
      const res = await axiosInstance.get(API_URL + "/auth/users/me/");
      dispatch(userSuccess(res.data));
    } catch (err) {
      const res = err.response.data.code;
      if (localStorage.getItem("refresh")) {
        if (res === "token_not_valid") {
          dispatch(refreshToken());
        }
      }
      dispatch(userFail());
    }
  } else {
    dispatch(userFail());
  }
};

export const refreshToken = () => async (dispatch) => {
  if (localStorage.getItem("refresh")) {
    try {
      const res = await axiosInstance.post(API_URL + "/auth/jwt/refresh/", { refresh: localStorage.getItem("refresh") });
      dispatch(refreshSuccess(res.data));
    } catch (err) {
      dispatch(userFail(err));
    }
  } else {
    dispatch(userFail());
  }
};

export const register = (email, username, password, re_password) => (dispatch) => {
  dispatch(setLoading(true));
  axios
    .post(API_URL + "/auth/users/", {
      username,
      email,
      password,
      re_password,
    })
    .then((res) => {
      dispatch(userRegisterSuccess());
      console.log("user register done");
      verify(res.uid, res.token);
      dispatch(load_user());
      dispatch(setLoading(false));
    })
    .catch((err) => {
      const errcode = err.response.data;
      errcode.email && dispatch(userFail(errcode.email[0]));
      errcode.password && dispatch(userFail(errcode.password[0]));
      errcode.username && dispatch(userFail(errcode.username[0]));
      errcode.non_field_errors && dispatch(userFail(errcode.non_field_errors));
      dispatch(setLoading(false));
    });
};
export const getUserInfo = (username) => async (dispatch) => {
  // console.log("running get user info");
  dispatch(setLoading(true));
  try {
    const res = await axiosInstance.get(API_URL + `/user/${username}/`);
    dispatch(profileUserSuccess(res.data));
    dispatch(setLoading(false));
    localStorage.setItem("userData", JSON.stringify(res));
    // console.log(localStorage.getItem("userData"));
  } catch (err) {
    console.log(err);
    dispatch(setLoading(false));
    // console.log(err);
  }
};

export const verify = (uid, token) => async (dispatch) => {
  dispatch(setLoading(true));
  try {
    await axiosInstance.post(API_URL + "/auth/users/activation/", {
      uid,
      token,
    });
    dispatch(setLoading(false));
  } catch (err) {
    dispatch(setLoading(false));
  }
};

export const userProfile = (username) => async (dispatch) => {
  dispatch(setLoading(true));
  try {
    const res = await axiosInstance.get(API_URL + `/user/${username}/`);
    dispatch(setLoading(false));
    dispatch(profileUserSuccess(res.data));
  } catch (err) {
    dispatch(userFail());
    dispatch(setLoading(false));
  }
};

export const login = (email, password) => async (dispatch) => {
  dispatch(setLoading(true));
  console.log(email);
  console.log(password);

  try {
    const res = await axios.post(API_URL + `/auth/token/jwt/create/`, {
      email,
      password,
    });
    dispatch(loginSuccess(res.data));
    localStorage.setItem("access", res.data.access);
    localStorage.setItem("refresh", res.data.refresh);
    console.log("login" + res.data);
    // localStorage.setItem("username", username);
    // console.log("username" + username);
    dispatch(load_user());
    dispatch(setLoading(false));
  } catch (err) {
    console.log(err);
    dispatch(userFail("User or password is wrong !"));
    dispatch(setLoading(false));
  }
};

export const checkAuthenticated = () => async (dispatch) => {
  if (localStorage.getItem("access")) {
    const config = {
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    };

    const body = JSON.stringify({ token: localStorage.getItem("access") });

    try {
      const res = await axios.post(API_URL + `auth/jwt/verify/`, body, config);

      if (res.data.code !== "token_not_valid") {
        dispatch(authSuccess());
      } else {
        dispatch(userFail());
      }
    } catch (err) {
      dispatch(userFail());
    }
  } else {
    dispatch(userFail());
  }
};

export const logoutAct = () => (dispatch) => {
  dispatch(logMeOut());
  // dispatch(load_user());
};
