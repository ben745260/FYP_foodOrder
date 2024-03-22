<template>
  <div v-if="salesData" class="mt-3">
    <v-expansion-panels class="mb-3">
      <v-expansion-panel @click="gptSalesPOST" color="blue-grey-lighten-4">
        <template #title>
          <span class="fw-bold fs-3">Sales Analysis Report</span>
        </template>
        <template #text>
          <div class="fs-5">
            <v-skeleton-loader
              v-if="!gptSales"
              type="text"
              :loading="true"
              height="28"
            ></v-skeleton-loader>
            <span v-else>{{ gptSales }}</span>
          </div>
        </template>
      </v-expansion-panel>
    </v-expansion-panels>
    <h3>Total Sales: ${{ salesData.totalSales }}</h3>
    <h3>Sales Trend:</h3>
    <div style="height: 500px">
      <canvas id="salesTrendChart"></canvas>
    </div>
  </div>
</template>
  
  <script>
import apiClient from "@/axios/apiClient";
import { generateDescription } from "@/methods/gpt/generateDescription";

import {
  Chart,
  LineController,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
} from "chart.js";

Chart.register(
  LineController,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement
);

export default {
  name: "SalesChart",
  data() {
    return {
      salesData: [],
      gptSales: null,
    };
  },
  mounted() {
    this.fetchSalesData();
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
    gptSalesPOST() {
      if (this.gptSales != null) {
        return;
      }
      let systemMsg =
        "You are a restaurant admin who reviewing the sales data of your restaurant";
      let userMsg = `Summarize this data of the total sales: ${
        this.salesData.totalSales
      } and monthly sales: ${JSON.stringify(
        this.salesData.salesTrend
      )}. Then give a sum up analysis result. Give me in one line`;
      let assisMsg = "";
      generateDescription(assisMsg, systemMsg, userMsg)
        .then((description) => {
          this.gptSales = description;
          // this.gptAnswer = description;
          // // console.log(description);
        })
        .catch((error) => {
          this.$toast.error(error, {
            duration: 6000,
          });
        });
    },
    createSalesTrendChart() {
      const ctx = document.getElementById("salesTrendChart").getContext("2d");
      new Chart(ctx, {
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
  },
};
</script>

<style scoped>
</style>