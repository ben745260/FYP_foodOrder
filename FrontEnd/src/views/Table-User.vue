<template>
  <v-layout>
    <v-app-bar color="primary" dark>
      <v-toolbar-title class="text-center">
        <span class="headline fs-2 fw-bolder" @click="$router.push('./tablemenu')">FoodDine</span>
      </v-toolbar-title>
    </v-app-bar>

    <v-app-bar color="light" dense>
      <v-tabs v-model="activeTab" background-color="light" color="primary">
        <v-tab v-for="tab in tabs" :key="tab.name" :to="tab.to" exact :exact-active-class="'active-link'">
          {{ tab.label }}
        </v-tab>
      </v-tabs>
    </v-app-bar>

    <v-main class="fixed">
      <router-view></router-view>
    </v-main>
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
        { name: "checkout", label: "Cart", to: "./checkout" },
        { name: "vieworder", label: "Record", to: "./vieworder" },
      ],
    };
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
  height: 87vh;
  margin-top: 13vh;
}
</style>