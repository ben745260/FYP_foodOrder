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
              <h2 class="card-title mb-4">Register</h2>
            </v-card-title>
            <v-card-text>
              <v-form @submit.prevent="submitForm">
                <v-text-field
                  v-model="username"
                  label="Username"
                  required
                ></v-text-field>
                <v-text-field
                  v-model="password"
                  label="Password"
                  type="password"
                  required
                ></v-text-field>
                <v-text-field
                  v-model="confirmPassword"
                  label="Confirm Password"
                  type="password"
                  required
                ></v-text-field>
                <v-btn type="submit" color="primary" block class="mb-3"
                  >Register</v-btn
                >
                <div class="text-center">
                  <small
                    >Already have an account?
                    <router-link to="/login">Login</router-link></small
                  >
                </div>
                <div
                  v-if="passwordMismatch"
                  class="text-center text-danger mt-2"
                >
                  Passwords do not match.
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
      confirmPassword: "",
      passwordMismatch: false,
    };
  },
  methods: {
    submitForm() {
      if (this.password !== this.confirmPassword) {
        this.passwordMismatch = true;
        return;
      }
      apiClient
        .post("/create-superuser/", {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          this.$router.push("/login");
        })
        .catch((error) => {
          // Handle registration error
          console.log(error.response.data.message);
          let response = error.response.data;
          for (let property in response) {
            if (response.hasOwnProperty(property)) {
              if (Array.isArray(response[property])) {
                response[property].forEach((errorMsg) => {
                  console.log(errorMsg);
                  this.$toast.error(errorMsg, {
                    duration: 6000,
                  });
                });
              } else {
                console.log(response[property]);
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