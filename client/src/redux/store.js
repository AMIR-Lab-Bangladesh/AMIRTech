import { configureStore } from "@reduxjs/toolkit";
import  userRegister  from "./slices/UserSlice";

const store = configureStore({
    reducer: {
        userReducer: userRegister,
    },
});
export default store;