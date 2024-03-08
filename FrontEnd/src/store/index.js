import { createStore } from 'vuex';
import createPersistedState from 'vuex-persistedstate';
import SecureLS from "secure-ls";
var ls = new SecureLS({ isCompression: false });

export default createStore({
  state() {
    return {
      isAuthenticated: false,
      isAdmin: false,
      token: '',
      username: '',
      cartItems: [], // New cartItems state to store the items in the cart
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
    addToCart(state, { productId, quantity }) {
      // Check if the product already exists in the cart
      const existingCartItem = state.cartItems.find(item => item.productId === productId);

      if (existingCartItem) {
        // If the product already exists, update its quantity
        existingCartItem.quantity += quantity;
      } else {
        // If the product does not exist, add it as a new item
        state.cartItems.push({ productId, quantity });
      }
    },
  },
  modules: {
  },
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