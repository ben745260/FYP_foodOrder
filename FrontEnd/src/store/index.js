import { createStore } from 'vuex';
import createPersistedState from 'vuex-persistedstate';

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
  plugins: [createPersistedState()],
});