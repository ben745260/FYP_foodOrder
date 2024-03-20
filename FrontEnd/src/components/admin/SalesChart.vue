<template>
    <div v-if="salesData" class="mt-3">
      <p>Total Sales: ${{ salesData.totalSales }}</p>
      <p>Sales Trend:</p>
      <canvas id="salesTrendChart"></canvas>
    </div>
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
        salesData: null,
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