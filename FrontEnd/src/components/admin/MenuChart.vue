<template>
  <div v-if="menuData" class="mt-3">
    <p>Most Popular Menu Items:</p>
    <canvas id="popularItemsChart"></canvas>
    <p>Item Profitability:</p>
    <canvas id="profitabilityChart"></canvas>
  </div>
</template>
  
  <script>
import apiClient from "@/axios/apiClient";
import {
  Chart,
  BarController,
  CategoryScale,
  LinearScale,
  BarElement,
} from "chart.js";

Chart.register(BarController, CategoryScale, LinearScale, BarElement);

export default {
  name: "MenuChart",
  data() {
    return {
      menuData: null,
    };
  },
  mounted() {
    this.fetchMenuData();
  },
  methods: {
    fetchMenuData() {
      apiClient.get("/menu-analysis/").then((response) => {
        this.menuData = response.data;
        this.$nextTick(() => {
          this.createProfitabilityChart();
        });
      });
    },
    createProfitabilityChart() {
      const popularItemsElement = document.getElementById("popularItemsChart");
      if (
        popularItemsElement &&
        this.menuData &&
        this.menuData.mostPopularItems
      ) {
        const ctx1 = popularItemsElement.getContext("2d");
        new Chart(ctx1, {
          type: "bar",
          data: {
            labels: this.menuData.mostPopularItems.map((entry) => entry.name),
            datasets: [
              {
                label: "Total Sales Quantity",
                data: this.menuData.mostPopularItems.map(
                  (entry) => entry.total_sales_quantity
                ),
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

      // Profitability Chart
      const profitabilityElement =
        document.getElementById("profitabilityChart");
      if (
        profitabilityElement &&
        this.menuData &&
        this.menuData.itemProfitability
      ) {
        const topTenItems = this.menuData.itemProfitability.slice(0, 10);
        const ctx2 = profitabilityElement.getContext("2d");
        new Chart(ctx2, {
          type: "bar",
          data: {
            labels: topTenItems.map((entry) => entry.name),
            datasets: [
              {
                label: "Profitability",
                data: topTenItems.map((entry) => entry.profitability),
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