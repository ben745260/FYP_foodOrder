import { createStore } from 'vuex';
import createPersistedState from 'vuex-persistedstate';
// import Cookies from "js-cookie"
import SecureLS from "secure-ls";
var ls = new SecureLS({ isCompression: false });

export default createStore({
  state() {
    return {
      isAuthenticated: false,
      isAdmin: false,
      token: '',
      username: '',
    };
  },
  mutations: {
    setToken(state, { token, username }) {
      state.token = token;
      state.username = username;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = '';
      state.username = '';
      state.isAdmin = false;
      state.isAuthenticated = false;
    },
  },
  actions: {
  },
  modules: {
  },
  // localStorage
  // plugins: [createPersistedState()],

  //Cookies
  // plugins: [
  //   createPersistedState({
  //     storage: {
  //       getItem: (key) => Cookies.get(key),
  //       setItem: (key, value) =>
  //         Cookies.set(key, value, { expires: 3, secure: true }),
  //       removeItem: (key) => Cookies.remove(key)
  //     }
  //   })
  // ]

  plugins: [
    createPersistedState({
      storage: {
        getItem: (key) => ls.get(key),
        setItem: (key, value) => ls.set(key, value),
        removeItem: (key) => ls.remove(key)
      }
    })
  ]
});