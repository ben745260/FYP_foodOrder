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
      cartTotalAmount: '0',
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
    addToCart(state, { productId, quantity, price }) {
      // Check if the product already exists in the cart
      const existingCartItem = state.cartItems.find(item => item.productId === productId);

      if (existingCartItem) {
        // If the product already exists, update its quantity and product_amount
        existingCartItem.quantity += quantity;
        existingCartItem.product_amount = existingCartItem.quantity * price;
      } else {
        // If the product does not exist, add it as a new item with product_amount
        const product_amount = quantity * price;
        state.cartItems.push({ productId, quantity, product_amount });
      }
      // Update the cartTotalAmount
      state.cartTotalAmount = state.cartItems.reduce((total, item) => total + item.product_amount, 0);

      // Save the updated cartItems state in local storage
      ls.set('cartItems', state.cartItems);
    },
    removeItem(state, productId) {
      state.cartItems = state.cartItems.filter(item => item.productId !== productId);
      // Update the cartTotalAmount
      state.cartTotalAmount = state.cartItems.reduce((total, item) => total + item.product_amount, 0);
      ls.set('cartItems', state.cartItems);
    },
    removeAllItems(state) {
      state.cartItems = [];
      state.cartTotalAmount= '0';
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