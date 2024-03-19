<template>
    <v-app>
      <v-card fluid class="m-3">
        <v-card-title>
          <span class="fs-1">Analysis</span>
        </v-card-title>
        <v-card-text>
          <v-tabs v-model="activeTab">
            <v-tab v-for="(tab, index) in tabs" :key="index" @click="changeTab(index)">
              {{ tab }}
            </v-tab>
          </v-tabs>
          <v-tab-item v-for="(tab, index) in tabs" :key="index" v-bind:value="index">
            <v-card v-if="activeTab === index">
              <v-card-text v-if="tab === 'Sales'">
                <h2>Sales Analysis</h2>
                <div v-if="salesData">
                  <p>Total Sales: {{ salesData.totalSales }}</p>
                  <p>Most Popular Category: {{ salesData.mostPopularCategory }}</p>
                  <p>Sales Trend:</p>
                  <ul>
                    <li v-for="entry in salesData.salesTrend" :key="entry.date">
                      Date: {{ entry.date }}, Sales: {{ entry.sales }}
                    </li>
                  </ul>
                </div>
              </v-card-text>
              <v-card-text v-if="tab === 'Menu'">
                <h2>Menu Analysis</h2>
                <div v-if="menuData">
                  <p>Most Popular Menu Items:</p>
                  <ul>
                    <li v-for="item in menuData.mostPopularItems" :key="item">
                      {{ item }}
                    </li>
                  </ul>
                  <p>Item Profitability:</p>
                  <ul>
                    <li v-for="item in menuData.itemProfitability" :key="item.name">
                      Name: {{ item.name }}, Profitability: ${{ item.profitability }}
                    </li>
                  </ul>
                </div>
              </v-card-text>
            </v-card>
          </v-tab-item>
        </v-card-text>
      </v-card>
    </v-app>
  </template>
  
  <script>
  import apiClient from "@/axios/apiClient";
  
  export default {
    name: "Analysis",
    data() {
      return {
        activeTab: 0,
        tabs: ["Sales", "Menu"],
        salesData: null,
        menuData: null,
      };
    },
    mounted() {
      this.fetchSalesData();
      this.fetchMenuData();
    },
    methods: {
      changeTab(index) {
        this.activeTab = index;
      },
      fetchSalesData() {
        // Perform an API request to fetch sales data
        apiClient.get("/sales-analysis/").then((response) => {
          this.salesData = response.data;
        });
      },
      fetchMenuData() {
        // Perform an API request to fetch menu data
        apiClient.get("/menu-analysis/").then((response) => {
          this.menuData = response.data;
        });
      },
    },
  };
  </script>
  
  <style></style>