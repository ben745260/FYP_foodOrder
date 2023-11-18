<template>
    <div class="container d-flex align-items-center justify-content-center">
      <div class="row justify-content-center">
        <div class="col-md-12">
          <div class="card">
            <div class="card-body">
              <h2 class="card-title text-center mb-4">Login</h2>
              <form @submit.prevent="login">
                <div class="mb-4">
                  <label for="email" class="form-label">Email</label>
                  <input type="email" class="form-control" id="email" v-model="email" required>
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
  export default {
    data() {
      return {
        email: '',
        password: ''
      };
    },
    methods: {
      login() {
        // Implement your login logic here
        // For simplicity, let's assume successful login and navigate to a protected page
        this.$router.push('/dashboard');
      }
    }
  };
  </script>
  
  <style scoped>
  .card {
    border: none;
    box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.1);
  }
  
  .card-title {
    font-size: 24px;
    font-weight: bold;
  }
  
  .btn-primary {
    background-color: #007bff;
    border-color: #007bff;
  }
  
  .btn-primary:hover {
    background-color: #0069d9;
    border-color: #0062cc;
  }
  
  .btn-primary:focus {
    box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.5);
  }
  </style>