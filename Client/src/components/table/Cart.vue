<template>
  <v-app>
    <v-container>
      <v-card>
        <v-card-title>
          My Cart ({{ cartItems.length }} items) <v-spacer></v-spacer> Total: ${{ totalAmount }}
          <v-btn variant="tonal" color="error" @click="confirmClearItems" style="float: right;" :disabled="cartItems.length <= 0">Clear all items</v-btn>
        </v-card-title>
        <v-card-text>
          <v-table>
            <thead>
              <tr>
                <th class="text-left">Name</th>
                <th class="text-left">Quantity</th>
                <th class="text-left">Price</th>
                <th class="text-left"></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in cartItems" :key="item.productId">
                <td class="product-name">
                  <strong>{{ getProductById(item.productId)?.product_name }}</strong>
                </td>
                <td>{{ item.quantity }}</td>
                <td>
                  ${{
                    item.quantity * getProductById(item.productId)?.price
                  }}
                </td>
                <td>
                  <button @click="removeItem(item.productId)">
                    <i class="fa-solid fa-trash" style="color:#B00020"></i>
                  </button>
                </td>
              </tr>
            </tbody>
          </v-table>
          <!-- <br>
          {{ cartItems }}
          <hr>
          {{ totalAmount }} -->
        </v-card-text>
      </v-card>
    </v-container>



    <!-- Confirmation Dialog -->
    <v-dialog v-model="confirmDialog" persistent max-width="500px">
      <v-card>
        <v-card-title class="headline">Clear All Items</v-card-title>
        <v-card-text>
          <span>Are you sure you want to clear all items from your cart?</span>
        </v-card-text>
        <v-card-actions class="justify-end">
          <v-btn color="error" text @click="clearAllItems">Confirm</v-btn>
          <v-btn text @click="confirmDialog = false">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-app>
</template>

<script>
import apiClient from "@/axios/apiClient";

export default {
  name: "Cart",
  data() {
    return {
      categories: [],
      products: [],
      cartItems: this.$store.state.cartItems,
      totalAmount: this.$store.state.cartTotalAmount,
      confirmDialog: false, // Control variable for the confirmation dialog
    };
  },
  mounted() {
    this.fetchCategories();
    this.fetchProducts();
  },
  methods: {
    fetchCategories() {
      apiClient
        .get("/productcategories/")
        .then((response) => {
          const categories = response.data.map((category) => ({
            category_id: category.category_id,
            name: category.name,
            icon: category.icon,
          }));
          this.categories = categories;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    fetchProducts() {
      apiClient
        .get("/products/")
        .then((response) => {
          this.products = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getProductById(productId) {
      return this.products.find((product) => product.product_id === productId);
    },
    removeItem(productId) {
      this.$store.commit("removeItem", productId);
      this.cartItems = this.$store.state.cartItems; // Fetch the updated cart items
      this.totalAmount = this.$store.state.cartTotalAmount;
      
    },
    confirmClearItems() {
      this.confirmDialog = true; // Show the confirmation dialog
    },
    clearAllItems() {
      this.$store.commit("removeAllItems");
      this.cartItems = this.$store.state.cartItems; // Fetch the updated cart items
      this.totalAmount = this.$store.state.cartTotalAmount;
      this.confirmDialog = false; // Close the confirmation dialog
    },
  },
};
</script>

<style scoped>
.product-name {
  word-break: break-word;
}
</style>