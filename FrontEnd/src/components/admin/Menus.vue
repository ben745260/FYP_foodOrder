<template>
  <div>
    <h1>All Products</h1>
    <div class="menu-container">
      <div v-for="product in products" :key="product.product_id" class="menu-item">
        <img class="menu-image" :src="product.image" alt="Product Image">
        <div class="menu-details">
          <h3>{{ product.product_name }}</h3>
          <p>Price: $&nbsp;{{ product.price }}</p>
          <p>Category: {{ getCategoryLabel(product.category) }}</p>
          <p>Detail: {{ product.product_detail }}</p>
          <p>Published Date: {{ product.pub_date }}</p>
        </div>
      </div>
    </div>

    <!-- Add New Product Button -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#addProductModal">
      Add New Product
    </button>

    <!-- Add Modal -->
    <div class="modal" id="addProductModal" tabindex="-1" role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add New Product</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form>
              <div class="form-group">
                <label for="productName">Product Name</label>
                <input type="text" class="form-control" id="productName" v-model="newProduct.product_name">
              </div>
              <div class="form-group">
                <label for="productPrice">Price</label>
                <input type="number" class="form-control" id="productPrice" v-model="newProduct.price">
              </div>
              <div class="form-group">
                <label for="productCategory">Category</label>
                <select class="form-control" id="productCategory" v-model="newProduct.category">
                  <option v-for="(categoryName, categoryId) in categories" :value="categoryId" :key="categoryId">{{
                    categoryName }}</option>
                </select>
              </div>
              <div class="form-group">
                <label for="productImage">Product Image</label>
                <input type="file" class="form-control-file" id="productImage" @change="handleImageUpload">
              </div>
              <div class="form-group">
                <label for="productDetail">Product Detail</label>
                <textarea class="form-control" id="productDetail" rows="5" v-model="newProduct.product_detail"></textarea>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary" @click="saveNewProduct">Save</button>
          </div>
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
      products: [],
      categories: {},
      newProduct: {
        product_name: '',
        price: null,
        category: null,
        image: null,
        product_detail: ''
      }
    };
  },
  mounted() {
    this.fetchProducts();
    this.fetchCategories();
  },
  methods: {
    fetchProducts() {
      apiClient.get('/products/')
        .then(response => {
          this.products = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    fetchCategories() {
      apiClient.get('/productcategories/')
        .then(response => {
          const categories = {};
          response.data.forEach(category => {
            categories[category.category_id] = category.name;
          });
          this.categories = categories;
        })
        .catch(error => {
          console.error(error);
        });
    },
    getCategoryLabel(category) {
      if (category in this.categories) {
        return this.categories[category];
      } else {
        return '';
      }
    },
    handleImageUpload(event) {
      const file = event.target.files[0];
      this.newProduct.image = file;
    },
    saveNewProduct() {
      // Check if the "Product Detail" and "Product Image" fields are null
      if (this.newProduct.product_name === null || this.newProduct.price === null|| this.newProduct.category === null) {
        // Display an error message or perform any necessary action
        // console.error('Product name and price are required');
        this.$toast.error('Product name, price, or category are required', {
          duration: 6000
        });
        return;
      }

      // Create a FormData object to send the product data as multipart/form-data
      const formData = new FormData();
      formData.append('product_name', this.newProduct.product_name);
      formData.append('price', this.newProduct.price);
      formData.append('category', this.newProduct.category);
      formData.append('image', this.newProduct.image);
      formData.append('product_detail', this.newProduct.product_detail);
      console.log(formData);
      apiClient.post('/products/', formData)
        .then(response => {
          // Handle the successful creation of the product
          console.log('Product created:', response.data);
          // Refresh the product list
          this.fetchProducts();
          // Close the modal
          const modal = bootstrap.Modal.getInstance(document.getElementById('addProductModal'));
          modal.hide();
          // location.reload();
        })
        .catch(error => {
          // Handle the error
          console.error('Error creating product:', error);
        });
    }
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

.modal-body {
  max-height: 400px;
  overflow-y: auto;
}
</style>