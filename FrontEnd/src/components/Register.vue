<template>
  <div class="container-fluid d-flex align-items-center justify-content-center">
    <div class="row justify-content-center">
      <div class="col-md-12">
        <h1 class="text-center mb-4">Food Ordering System</h1>
      </div>
      <div class="col-md-12">
        <div class="card">
          <div class="card-body">
            <h2 class="card-title text-center mb-4">Register</h2>
            <form @submit.prevent="submitFrom">
              <div class="mb-4">
                <label for="username" class="form-label">Username</label>
                <input type="text" class="form-control" id="username" v-model="username" required>
              </div>
              <div class="mb-4">
                <label for="password" class="form-label">Password</label>
                <input type="password" class="form-control" id="password" v-model="password" required>
              </div>
              <div class="mb-4">
                <label for="confirmPassword" class="form-label">Confirm Password</label>
                <input type="password" class="form-control" id="confirmPassword" v-model="confirmPassword" required>
              </div>
              <button type="submit" class="btn btn-primary w-100 mb-3">Register</button>
              <div class="text-center">
                <small>Already have an account? <router-link to="/login">Login</router-link></small>
              </div>
              <div v-if="passwordMismatch" class="text-center text-danger mt-2">
                Passwords do not match.
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { register } from '../methods/register';

export default {
  data() {
    return {
      username: '',
      password: '',
      confirmPassword: '',
      passwordMismatch: false
    };
  },
  methods: {
    submitFrom() {
      if (this.password !== this.confirmPassword) {
        this.passwordMismatch = true;
        return;
      }

      register({
        username: this.username,
        password: this.password
      }); // Pass the registerUser data object as an argument
    }
  }
};
</script>