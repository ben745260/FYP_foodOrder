<template>
    <div>
      <h1>Test Page</h1>
      <button @click="navigateToHome">Go to Home</button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      navigateToHome() {
        this.$router.push('/');
      },
    },
  };
  </script>