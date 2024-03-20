<template>
  <v-app>
    <v-card fluid class="m-3">
      <v-card-title>
        <v-tabs v-model="tab">
          <v-tab value="sales">Sales</v-tab>
          <v-tab value="menu">Menu</v-tab>
        </v-tabs>
      </v-card-title>
      <v-card-text>
        <v-window v-model="tab">
          <v-window-item value="sales">
            <SalesChart />
          </v-window-item>
          <v-window-item value="menu">
            <MenuChart />
          </v-window-item>
        </v-window>
      </v-card-text>
    </v-card>
  </v-app>
</template>

<script>
import SalesChart from './SalesChart.vue';
import MenuChart from './MenuChart.vue';

export default {
  name: "Analysis",
  components: {
    SalesChart,
    MenuChart
  },
  data() {
    return {
      tab: null,
    };
  },
};
</script>