<template>
  <v-layout>
    <v-app-bar color="primary" dark>
      <v-toolbar-title class="text-center">
        <span
          class="headline fs-2 fw-bolder"
          @click="$router.push('./tablemenu')"
          >FoodDine</span
        >
      </v-toolbar-title>
    </v-app-bar>

    <v-app-bar color="light" dense>
      <v-tabs v-model="activeTab" background-color="light" color="primary">
        <v-tab
          v-for="tab in tabs"
          :key="tab.name"
          :to="tab.to"
          exact
          :exact-active-class="'active-link'"
        >
          {{ tab.label }}
        </v-tab>
      </v-tabs>
    </v-app-bar>

    <v-main class="fixed">
      <router-view></router-view>
    </v-main>

    <v-footer color="primary" app>
      <v-btn @click="confirmOrder" variant="text" block class="text-center fs-5"
        >Order</v-btn
      >
    </v-footer>

    <!-- Confirmation Dialog -->
    <v-dialog v-model="confirmDialog" max-width="500px">
      <v-card>
        <v-card-title class="headline">Confirm Order</v-card-title>
        <v-card-text>
          <span>Are you sure you want to place the order?</span>
        </v-card-text>
        <v-card-actions class="justify-end">
          <v-btn color="primary" text @click="placeOrder">Confirm</v-btn>
          <v-btn text @click="cancelOrder">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
export default {
  name: "Table_User",
  data() {
    return {
      activeTab: "",
      tabs: [
        { name: "tablemenu", label: "Menu", to: "./tablemenu" },
        { name: "cart", label: "Cart", to: "./cart" },
        { name: "vieworder", label: "Record", to: "./vieworder" },
      ],
      confirmDialog: false, // Control variable for the confirmation dialog
    };
  },
  methods: {
    confirmOrder() {
      this.confirmDialog = true; // Show the confirmation dialog
    },
    placeOrder() {
      // Perform your order logic here
      this.confirmDialog = false; // Close the confirmation dialog
      this.$router.push("/order");
    },
    cancelOrder() {
      this.confirmDialog = false; // Close the confirmation dialog
    },
  },
};
</script>

<style scoped>
.header-link {
  font-size: 1.5rem;
  color: #fff;
  text-decoration: none;
  margin: 0 10px;
}

.active-link {
  font-weight: bold;
}

.v-main {
  padding-top: 20px;
  /* height: 87vh; */
  margin-top: 13vh;
}
</style>