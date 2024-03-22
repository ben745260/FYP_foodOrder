<template>
  <v-card>
    <v-layout>
      <v-navigation-drawer theme="dark" permanent>
        <v-list nav>
          <v-list-item>
            <h1>FoodDine<br>System</h1>
            <span class="fw-semibold">{{ username }}</span>
          </v-list-item>
          <v-divider></v-divider>
          <v-list-item link prepend-icon="mdi-view-dashboard" title="" :to="{ path: '/admin/dashboard' }" :class="{ active: isActive('/admin/dashboard') }">
            <span class="fw-semibold">Dashboard</span>
          </v-list-item>
          <v-list-item link prepend-icon="mdi-order-alphabetical-ascending" :to="{ path: '/admin/orders' }" :class="{ active: isActive('/admin/orders') }">
            <span class="fw-semibold">Orders</span>
          </v-list-item>
          <v-list-item link prepend-icon="mdi-table" title="" :to="{ path: '/admin/tables' }" :class="{ active: isActive('/admin/tables') }">
            <span class="fw-semibold">Tables</span>
          </v-list-item>
          <v-list-item link prepend-icon="mdi-menu" title="" :to="{ path: '/admin/menus' }" :class="{ active: isActive('/admin/menus') }">
            <span class="fw-semibold">Menus</span>
          </v-list-item>
          <v-list-item link prepend-icon="mdi-comment-quote" title="" :to="{ path: '/admin/userFeedback' }" :class="{ active: isActive('/admin/userFeedback') }">
            <span class="fw-semibold">User Feedback</span>
          </v-list-item>
          <v-list-item link prepend-icon="mdi-poll" title="" :to="{ path: '/admin/analysis' }" :class="{ active: isActive('/admin/analysis') }">
            <span class="fw-semibold">Analysis</span>
          </v-list-item>
          <v-list-item link prepend-icon="mdi-assistant" title="" :to="{ path: '/admin/assistantGPT' }" :class="{ active: isActive('/admin/assistantGPT') }">
            <span class="fw-semibold">Assistant GPT</span>
          </v-list-item>
        </v-list>

        <template v-slot:append>
          <div class="mb-5 px-3">
            <v-btn class="bg-blue-grey" block @click="logout"> Logout </v-btn>
          </div>
        </template>
      </v-navigation-drawer>
      <v-main>
        <router-view class="bg-grey-lighten-3"></router-view>
      </v-main>
    </v-layout>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      username: this.$store.state.username
    };
  },
  methods: {
    logout() {
      this.$store.commit("removeToken");
      location.reload(true);
    },
    isActive(route) {
      return this.$route.path === route;
    }
  }
};
</script>

<style scoped>
.v-list-item.active {
  background-color: #616161;
}
</style>