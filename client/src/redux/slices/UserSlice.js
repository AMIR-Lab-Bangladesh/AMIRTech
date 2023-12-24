import { createSlice } from "@reduxjs/toolkit";


const initialState={
    user:null,
    isLoading:false,
    error:null,
    isAuthenticated:false,
    access: localStorage.getItem('access'),
    refresh: localStorage.getItem('refresh'),
    message:null,
    profileUser:null,


};

export const userRegister = createSlice({
    name: "userRegister",
    initialState,
    reducers:{
        setLoading: (state, action)=>{
            state.isLoading = action.payload;

        },
        loginSuccess:(state, {payload})=>{
            state.access = payload.access;
            state.refresh = payload.refresh;
            state.isAuthenticated = true;
            state.isLoading = false;
            state.error = null;
        },
        refreshSuccess: (state, {payload})=>{
            state.access = localStorage.setItem("access", payload.access);
            state.isAuthenticated = true;
            state.isLoading = false;
            state.error = null;
        },
        userSuccess:(state, action)=>{
            state.user = action.payload;
            state.isAuthenticated = true;
            state.isLoading = false;
            state.error = null;
        },
        profileUserSuccess: (state, action)=>{
            state.profileUser = action.payload;
            state.isAuthenticated = true;
            state.isLoading = false;
            state.error = null;
        },
        removeMessage: (state, action)=>{
            state.message = null;
        },
        userRegisterSuccess:(state, action)=>{
            state.message =
        "Successfully registered ! Please confirm your email";
        },
        userFail:(state, { payload })=>{
            state.user = null;
            state.error = action.payload;
            state.isAuthenticated = false;
        },
        authSuccess: (state)=>{
            state.isAuthenticated = true;
        },
        setMeta:(state, {payload})=>{
            state.meta = payload;
        },
        logMeOut: (state) =>{
            localStorage.removeItem("access");
            localStorage.removeItem("refresh");
            state.user = null;
            state.access = null;
            state.refresh = null;
            state.isAuthenticated = false;
        },

    }});

    export const {
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
        logMeOut,
    } = userRegister.actions;
    
    export default userRegister.reducer;