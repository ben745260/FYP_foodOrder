<template>
  <v-app>
    <v-card fluid class="m-3">
      <v-card-title>
        <!-- <span class="fs-1">Analysis</span> -->
        <v-tabs v-model="tab">
          <v-tab value="sales">Sales</v-tab>
          <v-tab value="menu">Menu</v-tab>
        </v-tabs>
      </v-card-title>
      <v-card-text>
        <v-window v-model="tab">
          <v-window-item value="sales">
            <h2>2024 Sales Analysis</h2>
            <div v-if="salesData">
              <p>Total Sales: ${{ salesData.totalSales }}</p>
              <p>Sales Trend:</p>
              <canvas id="salesTrendChart"></canvas>
            </div>
          </v-window-item>

          <v-window-item value="menu">
            <h2>Menu Analysis</h2>
            <div v-if="menuData">
              <p>Most Popular Menu Items:</p>
              <ul>
                <li v-for="item in menuData.mostPopularItems" :key="item">
                  {{ item }}
                </li>
              </ul>
              <p>Item Profitability:</p>
              <canvas id="profitabilityChart"></canvas>
            </div>
          </v-window-item>
        </v-window>
      </v-card-text>
    </v-card>
  </v-app>
</template>
  
<script>
import apiClient from "@/axios/apiClient";
import {
  Chart,
  LineController,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
} from "chart.js";

Chart.register(
  LineController,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement
);

export default {
  name: "Analysis",
  data() {
    return {
      tab: null,
      salesData: null,
      menuData: null,
    };
  },
  mounted() {
    this.fetchSalesData();
    this.fetchMenuData();
  },
  methods: {
    fetchSalesData() {
      apiClient.get("/sales-analysis/").then((response) => {
        this.salesData = response.data;
        this.$nextTick(() => {
          this.createSalesTrendChart();
        });
      });
    },
    fetchMenuData() {
      apiClient.get("/menu-analysis/").then((response) => {
        this.menuData = response.data;
        this.$nextTick(() => {
          this.createProfitabilityChart();
        });
      });
    },
    createSalesTrendChart() {
      const ctx1 = document.getElementById("salesTrendChart").getContext("2d");
      new Chart(ctx1, {
        type: "line",
        data: {
          labels: this.salesData.salesTrend.map((entry) => {
            const monthNames = [
              "January",
              "February",
              "March",
              "April",
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "November",
              "December",
            ];
            return `${monthNames[entry.month - 1]}`;
          }),
          datasets: [
            {
              label: "Sales",
              data: this.salesData.salesTrend.map((entry) => entry.sales),
              fill: false,
              borderColor: "rgb(75, 192, 192)",
              tension: 0.1,
            },
          ],
        },
      });
    },
    createProfitabilityChart() {
      const chartElement = document.getElementById("profitabilityChart");
      if (chartElement) {
        const ctx2 = chartElement.getContext("2d");
        new Chart(ctx2, {
          type: "bar",
          data: {
            labels: this.menuData.profitability.map((entry) => entry.item),
            datasets: [
              {
                label: "Profitability",
                data: this.menuData.profitability.map((entry) => entry.profit),
                backgroundColor: "rgb(75, 192, 192)",
              },
            ],
          },
          options: {
            indexAxis: "y",
            scales: {
              x: {
                beginAtZero: true,
              },
            },
          },
        });
      }
    },
  },
};
</script>

<style></style>