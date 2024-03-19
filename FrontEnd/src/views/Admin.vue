<template>
  <v-card>
    <v-layout>
      <v-navigation-drawer theme="dark" permanent>
        <v-list nav>
          <v-list-item><h1>FoodDine<br>System</h1><span class="fw-semibold"> {{ username }}</span></v-list-item>
          <v-divider></v-divider>
          <v-list-item link prepend-icon="mdi-view-dashboard" title="" @click="$router.push('/admin/dashboard')"><span class="fw-semibold">Dashboard</span></v-list-item>
          <v-list-item link prepend-icon="mdi-order-alphabetical-ascending" @click="$router.push('/admin/orders')"><span class="fw-semibold">Orders</span></v-list-item>
          <v-list-item link prepend-icon="mdi-table" title="" @click="$router.push('/admin/tables')"><span class="fw-semibold" >Tables</span></v-list-item>
          <v-list-item link prepend-icon="mdi-menu" title="" @click="$router.push('/admin/menus')"><span class="fw-semibold">Menus</span></v-list-item>
          <v-list-item link prepend-icon="mdi-comment-quote" title="" @click="$router.push('/admin/userFeedback')"><span class="fw-semibold">User Feedback</span></v-list-item>
          <v-list-item link prepend-icon="mdi-poll" title="" @click="$router.push('/admin/analysis')"><span class="fw-semibold">Analysis</span></v-list-item>
        </v-list>

        <template v-slot:append>
          <div class="mb-5 px-3">
            <v-btn class="bg-blue-grey" block @click="logout"> Logout </v-btn>
          </div>
        </template>
      </v-navigation-drawer>
      <v-main >
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
      this.$store.commit('removeToken');
      location.reload(true);
    }
  }
};
</script>

<style scoped>
</style>