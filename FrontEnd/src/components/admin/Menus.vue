<template>
  <div>
    <div class="container-fluid h1">
      All Items
      <button type="button" class="btn btn-primary float-end align-bottom" data-bs-toggle="modal"
        data-bs-target="#addProductModal">
        Add New Item
      </button>
    </div>

    <div class="menu-container">
      <div v-for="product in products" :key="product.product_id" class="menu-item">
        <img class="menu-image" :src="product.image" alt="Product Image">
        <div class="menu-details">
          <h3>{{ product.product_name }}</h3>
          <p>Price: $&nbsp;{{ product.price }}</p>
          <p>Category: {{ getCategoryLabel(product.category) }}</p>
          <p>Desciption: {{ product.product_detail }}</p>
          <p>Published Date: {{ product.pub_date }}</p>
          <button type="button" class="btn btn-primary" data-bs-toggle="modal"
            :data-bs-target="'#editProductModal-' + product.product_id" @click="setEditProduct(product)">
            Edit
          </button>
        </div>
      </div>
    </div>

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
                <label for="productName">Name</label>
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
                <label for="productDetail">Desciption</label>
                <textarea class="form-control" id="productDetail" rows="5" v-model="newProduct.product_detail"></textarea>
              </div>
              <div class="form-group">
                <label for="productImage">Image<span class="text-secondary">(Optional)</span></label><br>
                <input type="file" class="form-control" id="productImage" @change="handleImageUpload_add">
                <div v-if="newProduct.imageUrl">
                  <img v-if="newProduct.imageUrl" :src="newProduct.imageUrl" class="uploaded-image" alt="Uploaded Image">
                </div>
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
    <!-- Edit Product Modal -->
    <div v-for="product in products" :key="product.product_id" :id="'editProductModal-' + product.product_id"
      class="modal fade" tabindex="-1" aria-labelledby="editProductModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="editProductModalLabel">{{ editProduct.product_name }}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <form @submit.prevent="updateProduct(product.product_id)">
            <div class="modal-body">
              <div class="form-group">
                <label for="editProductName">Product Name</label>
                <input type="text" class="form-control" id="editProductName" v-model="editProduct.product_name">
              </div>
              <div class="form-group">
                <label for="editProductPrice">Price</label>
                <input type="number" class="form-control" id="editProductPrice" v-model="editProduct.price">
              </div>
              <div class="form-group">
                <label for="editProductCategory">Category</label>
                <select class="form-control" id="editProductCategory" v-model="editProduct.category">
                  <option v-for="(categoryName, categoryId) in categories" :key="categoryId" :value="categoryId">{{
                    categoryName }}</option>
                </select>
              </div>
              <div class="form-group">
                <label for="editProductDetail">Desciption</label>
                <textarea class="form-control" id="editProductDetail" v-model="editProduct.product_detail"></textarea>
              </div>
              <div class="form-group">
                <label for="editProductImage">Image</label>
                <input type="file" class="form-control" id="editProductImage" @change="handleImageUpload_update($event)">
                <img :src="editProduct.imageUrl" class="uploaded-image" v-if="editProduct.imageUrl">
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-danger" @click="deleteProduct(product.product_id)">Delete</button>
              <button type="submit" class="btn btn-primary">Update</button>
            </div>
          </form>

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
      },
      editProduct: {
        product_id: null,
        product_name: '',
        price: null,
        category: null,
        image: null,
        product_detail: '',
        imageUrl: ''
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
    handleImageUpload_add(event) {
      const file = event.target.files[0];
      this.newProduct.image = file;

      // Read the file and display the image
      const reader = new FileReader();
      reader.onload = (e) => {
        this.newProduct.imageUrl = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    saveNewProduct() {
      // Check if the "Product Detail" field is null or empty
      if (
        !this.newProduct.product_name ||
        !this.newProduct.price ||
        !this.newProduct.category
      ) {
        this.$toast.error("Product name, price, or category are required", {
          duration: 6000,
        });
        return;
      }

      // Create a FormData object to send the product data as multipart/form-data
      const formData = new FormData();
      formData.append("product_name", this.newProduct.product_name);
      formData.append("price", this.newProduct.price);
      formData.append("category", this.newProduct.category);

      // Check if an image file is selected
      if (this.newProduct.image) {
        formData.append("image", this.newProduct.image);
      }

      formData.append("product_detail", this.newProduct.product_detail);

      apiClient
        .post("/products/", formData)
        .then((response) => {
          console.log("Product created:", response.data);
          this.fetchProducts();
          const modal = bootstrap.Modal.getInstance(
            document.getElementById("addProductModal")
          );
          modal.hide();

          this.$toast.success(this.newProduct.product_name + " added", {
            duration: 6000,
          });
        })
        .catch((error) => {
          console.error("Error creating product:", error);
        });
    },
    handleImageUpload_update(event) {
      const file = event.target.files[0];
      if (file) {
        this.editProduct.image = file;
        this.editProduct.imageUrl = URL.createObjectURL(file);
      } else {
        // No file selected, keep the original image
        this.editProduct.image = null;
      }
    },
    setEditProduct(product) {
      this.editProduct = {
        product_id: product.product_id,
        product_name: product.product_name,
        price: product.price,
        category: product.category,
        image: null,
        product_detail: product.product_detail,
        imageUrl: product.image
      };
    },
    updateProduct(productId) {
      // Exclude the image property if it hasn't been changed
      const updatedProduct = { ...this.editProduct };
      if (!updatedProduct.image) {
        delete updatedProduct.image;
      }

      apiClient.put(`/products/${productId}/`, updatedProduct)
        .then(response => {
          // Handle successful update
          console.log('Product updated successfully');
          // Refresh the product list
          this.fetchProducts();

          // Close the modal
          const modalId = `editProductModal-${productId}`;
          const modal = bootstrap.Modal.getInstance(document.getElementById(modalId));
          modal.hide();

          this.$toast.success(this.editProduct.product_name + " updated", {
            duration: 6000,
          });
        })
        .catch(error => {
          console.error(error);
          // Handle error
        });
    },
    deleteProduct(productId) {
      if (confirm('Are you sure you want to delete this product?')) {
        apiClient.delete(`/products/${productId}/`)
          .then(() => {
            console.log('Product deleted successfully');
            // Refresh the product list
            this.fetchProducts();

            // Close the modal
            const modalId = `editProductModal-${productId}`;
            const modal = bootstrap.Modal.getInstance(document.getElementById(modalId));
            modal.hide();
            this.$toast.success(this.editProduct.product_name + " deleted", {
            duration: 6000,
          });
          })
          .catch(error => {
            console.error(error);
            // Handle error
          });
      }
    }
  }
};
</script>

<style scoped>
.menu-container {
  height:90vh;
  display: flex;
  flex-wrap: wrap;
  overflow-y: scroll;
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
  max-height: 800px;
  overflow-y: auto;
}

.form-group {
  margin-bottom: 10px;
}

.uploaded-image {
  max-width: 200px;
  margin-top: 10px;
}
</style>