import { createStore } from 'vuex';
import createPersistedState from 'vuex-persistedstate';

export default createStore({
  state() {
    return {
      isAuthenticated: false,
      isAdmin: false,
      token: '',
    };
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = '';
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