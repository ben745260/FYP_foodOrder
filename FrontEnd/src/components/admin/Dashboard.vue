<template>
  <v-app>
    <v-card fluid class="m-3">
      <v-card-title>
        <span class="fs-1">Dashboard</span>
      </v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="6">
            <v-card  :variant="'outlined'">
              <v-card-text class="text-center">
                <h2>Last Week Orders</h2>
                <h1>{{ dashboardData.lastweek_orders }}</h1>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="6">
            <v-card  :variant="'outlined'">
              <v-card-text class="text-center">
                <h2>Last Week Sales</h2>
                <h1>${{ dashboardData.lastweek_sales }}</h1>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <v-card  :variant="'outlined'">
              <v-card-text>
                <h2>Last Orders</h2>
                <v-data-table
                  :headers="lastOrdersHeaders"
                  :items="dashboardData.last_orders"
                  hide-default-footer
                >
                  <template #item="{ item }">
                    <tr>
                      <td>{{ item.order_id }}</td>
                      <td>{{ item.order_table }}</td>
                      <td>{{ item.order_lastUpdateDate }}</td>
                      <td>
                        {{ item.order_lastUpdateTime }}
                      </td>
                      <td>${{ item.order_amount }}</td>
                      <td>
                        <v-icon v-if="item.order_checkout" color="green">
                          mdi-check-circle
                        </v-icon>
                        <v-icon v-else color="red"> mdi-close-circle </v-icon>
                      </td>
                    </tr>
                  </template>
                </v-data-table>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <v-card  :variant="'outlined'">
              <v-card-text>
                <h2>Top Selling Products</h2>
                <v-data-table
                  :headers="topSellingProductsHeaders"
                  :items="dashboardData.top_selling_products"
                  hide-default-footer
                >
                  <template v-slot:items="props">
                    <td>{{ props.item.product_id__product_name }}</td>
                    <td>{{ props.item.product_id__category__name }}</td>
                    <td>{{ props.item.total_quantity }}</td>
                  </template>
                </v-data-table>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-app>
</template>
  
  <script>
import apiClient from "@/axios/apiClient";

export default {
  name: "Dashboard",
  data() {
    return {
      dashboardData: {},
      topSellingProductsHeaders: [
        { title: "Product Name", value: "product_id__product_name" },
        { title: "Product Category", value: "product_id__category__name" },
        { title: "Quantity", value: "total_quantity" },
      ],
      lastOrdersHeaders: [
        { title: "Order ID",  },
        { title: "Table", value: "order_table" },
        { title: "Date"},
        { title: "Time"},
        { title: "Amount" },
        { title: "Checkout"},
      ],
    };
  },
  mounted() {
    this.fetchDashboardData();
    setInterval(this.fetchDashboardData, 10000);
  },
  methods: {
    fetchDashboardData() {
      apiClient
        .get("/dashboard/")
        .then((response) => {
          this.dashboardData = response.data;
          this.dashboardData.last_orders.forEach((order) => {
            order.order_lastUpdateTime = order.order_lastUpdateTime.substring(
              0,
              8
            );
          });
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
  },
};
</script>