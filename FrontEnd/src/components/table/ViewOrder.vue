<template>
  <v-app>
    <v-container>
      <v-card>
        <v-card-title> My Order </v-card-title>
        <v-card-text>
          <v-table>
            <thead>
              <tr>
                <th class="text-left">Order ID</th>
                <th class="text-left">Product</th>
                <th class="text-left">Quantity</th>
                <th class="text-left">Product Amount</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="orderItem in orderItems" :key="orderItem.product">
                <td>{{ orderItem.order_id }}</td>
                <td>
                  {{ getProductById(orderItem.product_id)?.product_name }}
                </td>
                <td>{{ orderItem.quantity }}</td>
                <td>{{ orderItem.product_amount }}</td>
              </tr>
            </tbody>
          </v-table>
        </v-card-text>
      </v-card>
    </v-container>
  </v-app>
</template>
  
  <script>
import apiClient from "@/axios/apiClient";

export default {
  name: "ViewOrder",
  data() {
    return {
      orderItems: [],
      products: [], // Add products data
    };
  },
  mounted() {
    this.fetchOrderItems();
    this.fetchProducts();
  },
  methods: {
    fetchOrderItems() {
      // Make a GET request to retrieve the orders
      apiClient
        .get("/orders/")
        .then((response) => {
          // Filter the orders to find the orders with order_table = 1
          const orders = response.data.filter(
            (order) => order.order_table == "1"
          );

          // Extract the order IDs from the filtered orders
          const orderIds = orders.map((order) => order.order_id);

          // Make a GET request to retrieve the order items for each order ID
          const orderItemPromises = orderIds.map((orderId) => {
            return apiClient.get(`/orders/${orderId}/items/`);
          });

          // Execute all the order item requests concurrently
          Promise.all(orderItemPromises)
            .then((orderItemResponses) => {
              const orderItems = orderItemResponses.map(
                (response) => response.data
              );
              this.orderItems = orderItems.flat(); // Flatten the nested arrays
            })
            .catch((error) => {
              console.error("Failed to fetch order items:", error);
            });
        })
        .catch((error) => {
          console.error("Failed to fetch orders:", error);
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
  },
};
</script>
  
  <style>
/* Add your table styling here */
</style>