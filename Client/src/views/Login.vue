<template>
  <div class="d-flex align-items-center bg-grey-lighten-3" style="height: 100vh">
    <v-container fluid class="">
      <v-row justify="center">
        <v-col cols="12">
          <h1 class="text-center mb-4">FoodDine System</h1>
        </v-col>
        <v-col cols="12">
          <v-card class="w-50 mx-auto">
            <v-card-title class="text-center">
              <h2 class="card-title mb-4">Login</h2>
            </v-card-title>
            <v-card-text>
              <v-form @submit.prevent="submitForm">
                <v-row>
                  <v-col cols="12" md="12">
                    <v-text-field
                      v-model="username"
                      label="Username"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" md="12">
                    <v-text-field
                      v-model="password"
                      label="Password"
                      type="password"
                      required
                    ></v-text-field>
                  </v-col>
                </v-row>
                <v-btn type="submit" color="primary" block class="mb-3"
                  >Login</v-btn
                >
                <div class="text-center">
                  <small
                    >Don't have an account?
                    <router-link to="/register">Register</router-link></small
                  >
                </div>
              </v-form>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import apiClient from "@/axios/apiClient";

export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    submitForm() {
      apiClient
        .post("/token/login/", {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          this.$toast.success("Welcome, "+this.username, {
            duration: 6000,
          });
          const token = response.data.auth_token;
          this.$store.commit("setToken", { token, username: this.username });
          this.$router.push("/admin/dashboard");

          // this.$router.push("/admin/orders");
        })
        .catch((error) => {
          // Handle login error
          let response = error.response.data;
          for (let property in response) {
            if (response.hasOwnProperty(property)) {
              if (Array.isArray(response[property])) {
                response[property].forEach((errorMsg) => {
                  this.$toast.error(errorMsg, {
                    duration: 6000,
                  });
                });
              } else {
                this.$toast.error(response[property], {
                  duration: 6000,
                });
              }
            }
          }
        });
    },
  },
};
</script>

<style scoped>
</style>