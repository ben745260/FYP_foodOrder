<template>
    <div>
      <h1>Token: {{ token }}</h1>
    </div>
  </template>
  
  <script>
  import { mapState } from 'vuex';
  
  export default {
    computed: {
      ...mapState(['token']),
    },
  };
  </script>
  
  <style>
  /* Your styles here */
  </style>