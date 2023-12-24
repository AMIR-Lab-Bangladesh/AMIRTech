import {
    setLoading,
    loginSuccess,
    refreshSuccess,
    userSuccess,
    profileUserSuccess,
    removeMessage,
    userRegisterSuccess,
    userFail,
    authSuccess,
    setMeta,
    logMeOut
} from '../slices/UserSlice.js';

import axios from 'axios';
import {  axiosInstance } from '../../index';
import API_URL from '../../config.jsx';


export const load_user = () => async (dispatch) =>{
    if(localStorage.getItem("access")){
        try{
            const res = await axiosInstance.get( API_URL + "/auth/users/me/");
            dispatch(userSuccess(res.data))
        }
    }
    catch(err){
        const res = err.response.data.code;
      if (localStorage.getItem("refresh")) {
        if (res === "token_not_valid") {
          dispatch(refreshToken());
        }
      }
      dispatch(userFail());
    }
}



