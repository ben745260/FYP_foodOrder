<template>
  <v-app>
    <v-container>
      <v-card
        v-for="(orderItems, orderId, index) in groupedOrderItems"
        :key="orderId"
        class="mb-3"
      >
        <v-card-title>
          Order:&nbsp; {{ index + 1 }}<br>
          <span
            >Last Updated: {{ getLastUpdateTime(orderId) }}</span
          ></v-card-title
        >
        <v-card-text>
          <v-table>
            <thead>
              <tr>
                <th class="text-left">Product</th>
                <th class="text-left">Quantity</th>
                <th class="text-left">Product Amount</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="orderItem in orderItems" :key="orderItem.product_id">
                <td>
                  {{ getProductById(orderItem.product_id)?.product_name }}
                </td>
                <td>{{ orderItem.quantity }}</td>
                <td>$&nbsp;{{ orderItem.product_amount }}</td>
              </tr>
            </tbody>
          </v-table>
          <v-divider></v-divider>
          <h5 class="float-right">Total: $&nbsp;{{ getAmount(orderId) }}</h5>
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
      products: [],
      orderLastUpdateTimes: [], // Add order last update times object
      orderAmount: [],
    };
  },
  computed: {
    groupedOrderItems() {
      const groupedItems = {};

      // Group the order items by order ID
      this.orderItems.forEach((orderItem) => {
        const orderId = orderItem.order_id;
        if (!groupedItems[orderId]) {
          groupedItems[orderId] = [];
        }
        groupedItems[orderId].push(orderItem);
      });

      return groupedItems;
    },
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
          orders.forEach((order) => {
            const orderId = order.order_id;
            const lastUpdateTime = order.order_lastUpdateTime;
            this.orderLastUpdateTimes[orderId] = lastUpdateTime;
            const amount = order.order_amount;
            this.orderAmount[orderId] = amount;
          });
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

              // Save the last update time for each order ID
              this.orderItems.forEach((orderItem) => {
                const orderId = orderItem.order_id;
              });
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
    getLastUpdateTime(orderId) {
      const lastUpdateTime = this.orderLastUpdateTimes[orderId];
      if (lastUpdateTime) {
        // Format the last update time as desired (adjust the format according to your needs)
        return new Date(lastUpdateTime).toLocaleString();
      }
      return "Unknown";
    },
    getAmount(orderId) {
      const amount = this.orderAmount[orderId];
      if (amount) {
        return amount;
      }
      return "Unknown";
    },
  },
};
</script>

<style>
</style>