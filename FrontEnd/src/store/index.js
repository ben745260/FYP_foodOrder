import { createStore } from 'vuex'

export default createStore({
  state: {
    isAuthenticated: false,
    isAdmin: false,
    token: '',
  },
  mutations: {
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.isAdmin = false
      state.isAuthenticated = false
    },
  },
  actions: {
  },
  modules: {
  }
})
