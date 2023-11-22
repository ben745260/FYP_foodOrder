<template>
    <div>
      <h1>All Products</h1>
      <div class="menu-container">
        <div v-for="product in products" :key="product.product_id" class="menu-item">
            <img class="menu-image" :src="product.image" alt="Product Image">
          <div class="menu-details">
            <h3>{{ product.product_name }}</h3>
            <p>Price: {{ product.price }}</p>
            <p>Category: {{ product.category }}</p>
            <p>Published Date: {{ product.pub_date }}</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import apiClient from '@/axios/apiClient';
  
  export default {
    name: 'Menus',
    data() {
      return {
        products: []
      };
    },
    mounted() {
      apiClient.get('/products/')
        .then(response => {
          this.products = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
  };
  </script>
  
  <style scoped>
  .menu-container {
    display: flex;
    flex-wrap: wrap;
  }
  
  .menu-item {
    margin: 20px;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 4px;
    display: flex;
  }
  
  .menu-image {
    width: 150px;
    height: 150px;
    margin-right: 20px;
  }
  
  .menu-details {
    flex-grow: 1;
  }
  
  .menu-details h3 {
    margin-top: 0;
  }
  
  .menu-details p {
    margin-bottom: 5px;
  }
  </style>