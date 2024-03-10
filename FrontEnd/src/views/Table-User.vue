<template>
  <v-layout>
    <v-app-bar color="primary" dark>
      <v-toolbar-title class="text-center">
        <span
          class="headline fs-2 fw-bolder"
          @click="$router.push('./tablemenu')"
          >FoodDine</span
        >
      </v-toolbar-title>
    </v-app-bar>

    <v-app-bar color="light" dense>
      <v-tabs v-model="activeTab" background-color="light" color="primary">
        <v-tab
          v-for="tab in tabs"
          :key="tab.name"
          :to="tab.to"
          exact
          :exact-active-class="'active-link'"
        >
          {{ tab.label }}
        </v-tab>
      </v-tabs>
    </v-app-bar>

    <v-main class="fixed">
      <router-view></router-view>
    </v-main>

    <v-footer color="primary" app>
      <v-btn @click="confirmOrder" variant="text" block class="text-center fs-5"
        >Order</v-btn
      >
    </v-footer>

    <!-- Confirmation Dialog -->
    <v-dialog v-model="confirmDialog" max-width="500px">
      <v-card>
        <v-card-title class="headline">Confirm Order</v-card-title>
        <v-card-text>
          <span>Are you sure you want to place the order?</span>
        </v-card-text>
        <v-card-actions class="justify-end">
          <v-btn color="primary" text @click="placeOrder">Confirm</v-btn>
          <v-btn text @click="cancelOrder">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
import apiClient from "@/axios/apiClient";

export default {
  name: "Table_User",
  data() {
    return {
      activeTab: "",
      tabs: [
        { name: "tablemenu", label: "Menu", to: "./tablemenu" },
        { name: "cart", label: "Cart", to: "./cart" },
        { name: "vieworder", label: "Record", to: "./vieworder" },
      ],
      confirmDialog: false, // Control variable for the confirmation dialog
      cartItems: this.$store.state.cartItems,
      totalAmount: this.$store.state.cartTotalAmount,
    };
  },
  methods: {
    confirmOrder() {
      this.$router.push("./cart");
      this.confirmDialog = true; // Show the confirmation dialog
    },
    placeOrder() {
      // Assuming you have the necessary order and order items data in the component's data
      const orderData = {
        order_table: "1", // Replace with the user ID or username
        order_amount: this.totalAmount, // Replace with the total order amount
        // Add other required fields for the order
      };

      const orderItemsData = this.cartItems.map((cartItem) => {
        return {
          order_id: "", // Placeholder value, will be updated later
          product_id: cartItem.productId, // Replace with the product ID
          quantity: cartItem.quantity,
          product_amount: cartItem.product_amount, // Replace with the individual product amount
        };
      });

      // Make a POST request to the backend API to place the order
      apiClient
        .post("/orders/", orderData)
        .then((orderResponse) => {
          // Handle the successful order creation response
          console.log("Order placed successfully:", orderResponse.data);
          const orderId = orderResponse.data.order_id; // Replace with the correct ID field name
          console.log(orderId);

          // Update the order_id field in each orderItemData object
          orderItemsData.forEach((orderItemData) => {
            orderItemData.order_id = orderId;
          });

          // Create order items for the order
          const orderItemsPromises = orderItemsData.map((orderItemData) =>
            apiClient.post(
              `/orders/${orderId}/items/`,
              orderItemData
            )
          );

          // Wait for all order items to be created
          Promise.all(orderItemsPromises)
            .then((orderItemsResponses) => {
              // Handle the successful order items creation response
              console.log(
                "Order items created successfully:",
                orderItemsResponses.map((res) => res.data)
              );
              this.confirmDialog = false; // Close the confirmation dialog

              this.$store.commit("removeAllItems");
              this.cartItems = this.$store.state.cartItems; // Fetch the updated cart items
              this.totalAmount = this.$store.state.cartTotalAmount;
              this.confirmDialog = false; // Close the confirmation dialog

              this.$router.push("./vieworder");
            })
            .catch((error) => {
              // Handle the error case when creating order items
              console.error("Failed to create order items:", error);
            });
        })
        .catch((error) => {
          // Handle the error case when creating the order
          console.error("Failed to place order:", error);
        });
    },
    cancelOrder() {
      this.confirmDialog = false; // Close the confirmation dialog
    },
  },
};
</script>

<style scoped>
.header-link {
  font-size: 1.5rem;
  color: #fff;
  text-decoration: none;
  margin: 0 10px;
}

.active-link {
  font-weight: bold;
}

.v-main {
  padding-top: 20px;
  /* height: 87vh; */
  margin-top: 13vh;
}
</style>