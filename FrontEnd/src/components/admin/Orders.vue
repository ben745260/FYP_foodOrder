<template>
  <v-app>
    <v-card fluid class="m-3">
      <v-card-title>
        <span class="fs-1">Orders</span>
      </v-card-title>
      <v-card-text>
        <v-data-table :headers="headers" :items="orders.slice().reverse()">
          <template #item="{ item }">
            <tr>
              <td>{{ item.order_id }}</td>
              <td>
                {{ item.order_lastUpdateTime.substring(0, 8) }},
                {{ item.order_lastUpdateDate }}
              </td>
              <td>{{ item.order_table }}</td>
              <td>
                <v-row
                  v-for="orderItem in item.order_items"
                  :key="orderItem.product_id"
                  dense
                >
                  <v-col cols="4"
                    >{{ getProductById(orderItem.product_id)?.product_name }}
                  </v-col>
                  <v-col cols="4">x{{ orderItem.quantity }}</v-col>
                  <v-col cols="4">${{ orderItem.product_amount }}</v-col>
                </v-row>
              </td>
              <td>${{ item.order_amount }}</td>
              <td>
                <v-btn icon small @click="openDeleteOrderDialog(item)">
                  <v-icon>mdi-delete-forever</v-icon>
                </v-btn>
              </td>
            </tr>
          </template>
        </v-data-table>
      </v-card-text>
    </v-card>

    <v-dialog v-model="deleteOrderDialog" max-width="500px">
      <v-card>
        <v-card-title class="headline"
          >Delete Order:&nbsp;{{ deleteOrderId }}</v-card-title
        >
        <v-card-text>
          <span>Are you sure you want to delete {{ deleteOrderId }}?</span>
        </v-card-text>
        <v-card-actions>
          <v-btn color="error" text @click="deleteOrder">Confirm</v-btn>
          <v-btn text @click="closeDeleteOrderDialog">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-app>
</template>
  
  <script>
import apiClient from "@/axios/apiClient";

export default {
  name: "Orders",
  data() {
    return {
      orders: [],
      headers: [
        { title: "Order", value: "order_id", sortable: true },
        { title: "Order Time", value: "order_lastUpdateTime", sortable: false },
        { title: "Order Table", value: "order_table", sortable: true },
        { title: "Order Items", value: "order_items", sortable: false },
        { title: "Total Amount", value: "order_amount", sortable: true },
        { title: "Delete", value: "delete", sortable: false },
      ],
      products: [],
      deleteOrderDialog: false,
      deleteOrderId: "",
    };
  },
  mounted() {
    this.fetchOrderItems();
    this.fetchProducts();
    setInterval(this.fetchOrderItems, 5000);
  },
  methods: {
    fetchOrderItems() {
      // Make a GET request to retrieve the orders
      apiClient
        .get("/orders/")
        .then((response) => {
          this.orders = response.data;
          console.log(this.orders);
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
    openDeleteOrderDialog(order) {
      this.deleteOrderId = order.order_id;

      this.deleteOrderDialog = true;
    },
    closeDeleteOrderDialog() {
      this.deleteOrderDialog = false;
    },
    deleteOrder() {
      apiClient
        .delete(`/orders/${this.deleteOrderId}/`)
        .then(() => {
          console.log("Order deleted successfully");
          // Refresh the product list
          this.fetchOrderItems();
          this.$toast.success("Order" + this.deleteOrderID + " deleted", {
            duration: 6000,
          });
          this.deleteOrderId = "";
          this.deleteOrderDialog = false;
        })
        .catch((error) => {
          console.error(error);
          // Handle error
        });
    },
  },
};
</script>