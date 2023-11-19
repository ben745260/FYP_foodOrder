<template>
  <div class="container-fluid d-flex align-items-center justify-content-center">
    <div class="row justify-content-center">
      <div class="col-md-12">
        <h1 class="text-center mb-4">Food Ordering System</h1>
      </div>
      <div class="col-md-12">
        <div class="card">
          <div class="card-body">
            <h2 class="card-title text-center mb-4">Login</h2>
            <form @submit.prevent="submitFrom">
              <div class="mb-4">
                <label for="username" class="form-label">Username</label>
                <input type="text" class="form-control" id="username" v-model="username" required>
              </div>
              <div class="mb-4">
                <label for="password" class="form-label">Password</label>
                <input type="password" class="form-control" id="password" v-model="password" required>
              </div>
              <button type="submit" class="btn btn-primary w-100 mb-3">Login</button>
              <div class="text-center">
                <small>Don't have an account? <router-link to="/register">Register</router-link></small>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { login } from '../methods/login';


export default {
  data() {
    return {
      username: '', // Changed variable name from "email" to "username"
      password: ''
    };
  },
  methods: {
    submitFrom() {
      login({
        username: this.username,
        password: this.password
      });
    }
  }
};
</script>

<style scoped>
</style>