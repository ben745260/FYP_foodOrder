<template>
  <div v-if="menuData" class="mt-3">
    <v-expansion-panels class="mb-3">
      <v-expansion-panel @click="gptMenuPOST" color="blue-grey-lighten-4">
        <template #title>
          <span class="fw-bold fs-3">Menu Analysis Report</span>
        </template>
        <template #text>
          <div class="fs-5">
            <v-skeleton-loader
              v-if="!gptMenu"
              type="text"
              :loading="true"
              height="28"
            ></v-skeleton-loader>
            <span v-else>{{ gptMenu }}</span>
          </div>
        </template>
      </v-expansion-panel>
    </v-expansion-panels>
    <h3>Most Popular Menu Items:</h3>
    <div style="height: 500px">
      <canvas id="popularItemsChart"></canvas>
    </div>
    <h3>Item Profitability:</h3>
    <div style="height: 500px">
      <canvas id="profitabilityChart"></canvas>
    </div>
  </div>
</template>
  
  <script>
import apiClient from "@/axios/apiClient";
import { generateDescription } from "@/methods/gpt/generateDescription";

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
      menuData: [],
      gptMenu: null,
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
    gptMenuPOST() {
      if (this.gptMenu != null) {
        return;
      }
      let systemMsg =
        "You are a restaurant admin who reviewing the menu data of your restaurant";
      let userMsg = `Summarize this data of the mostPopularItems: ${
        this.menuData.mostPopularItems
      } and itemProfitability: ${JSON.stringify(
        this.menuData.itemProfitability
      )}. Then give a sum up analysis result. Give me in single line`;
      let assisMsg = "";
      generateDescription(assisMsg, systemMsg, userMsg)
        .then((description) => {
          this.gptMenu = description;
          // this.gptAnswer = description;
          // // console.log(description);
        })
        .catch((error) => {
          this.$toast.error(error, {
            duration: 6000,
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