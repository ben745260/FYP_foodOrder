<template>
  <v-app>
    <v-card fluid class="m-3">
      <v-card-title>
        <span class="fs-1">Menus</span>
        <v-btn color="primary" class="float-right" @click="openAddProductDialog"
          >Add Product</v-btn>
        <v-btn
          color="primary"
          class="float-right me-3"
          @click="openAddCategoryDialog"
          >Add Category</v-btn>
      </v-card-title>
      <v-card-text>
        <v-data-table
          :headers="headers"
          :items="products"
          :items-per-page="10"
          :footer-props="{
            showFirstLastPage: true,
            itemsPerPageOptions: [10, 20, 50, -1],
            itemsPerPageText: 'Items per page',
            itemsPerPageAllText: 'All',
          }"
          class="elevation-1"
        >
          <template #item="{ item }">
            <tr>
              <td>{{ item.product_name }}</td>
              <td>{{ getCategoryLabel(item.category) }}</td>
              <td>{{ item.price }}</td>
              <td>{{ item.product_detail }}</td>
              <td>{{ item.pub_date }}</td>
              <td>
                <v-btn
                  v-if="item.image"
                  icon
                  small
                  @click="openImageDialog(item.image)"
                >
                  <v-icon>mdi-eye</v-icon>
                </v-btn>
              </td>
              <td>
                <v-btn icon small>
                  <v-icon>mdi-pencil</v-icon>
                </v-btn>
              </td>
            </tr>
          </template>
        </v-data-table>
      </v-card-text>
    </v-card>
    <v-dialog v-model="imageDialog" max-width="500px">
      <v-card>
        <v-card-title> Image </v-card-title>
        <v-card-text>
          <v-img :src="selectedImage" contain></v-img>
        </v-card-text>
        <v-card-actions>
          <v-btn text @click="closeImageDialog">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="addCategoryDialog" max-width="500px">
      <v-card>
        <v-card-title> Add Category </v-card-title>
        <v-card-text>
          <v-text-field
            v-model="newCategoryName"
            label="Category Name"
          ></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="addCategory">Add</v-btn>
          <v-btn text @click="closeAddCategoryDialog">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="addProductDialog" max-width="500px">
      <v-card>
        <v-card-title> Add Product{{ categories }} </v-card-title>
        <v-card-text>
          <!-- Add your form fields here -->
          <v-text-field
            v-model="productName"
            label="Product Name"
          ></v-text-field>
          <!-- <v-select
            v-model="productCategory"
            :items="categories"
            label="Product Category"
          ></v-select> -->
          <v-text-field
            v-model="productPrice"
            label="Product Price"
          ></v-text-field>
          <v-textarea
            v-model="productDescription"
            label="Product Description"
          ></v-textarea>
          <v-text-field
            v-model="productImage"
            label="Product Image URL"
          ></v-text-field>
          <!-- Add more fields as needed -->
        </v-card-text>
        <v-card-actions>
          <v-btn text @click="closeAddProductDialog">Cancel</v-btn>
          <v-btn color="primary" @click="addProduct">Add</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-app>
</template>

<script>
import apiClient from "@/axios/apiClient";

export default {
  data() {
    return {
      products: [],
      categories: {},
      headers: [
        { title: "Product Name", value: "product_name", sortable: true },
        { title: "Category", value: "category", sortable: true },
        { title: "Price", value: "price", sortable: true },
        { title: "Description", value: "product_detail", sortable: true },
        { title: "Published Date", value: "pub_date", sortable: true },
        { title: "Image", value: "imageUrl", sortable: false },
        { title: "View Image", value: "viewImage", sortable: false },
      ],
      imageDialog: false,
      selectedImage: "",
      addCategoryDialog: false,
      newCategoryName: "",
      addProductDialog: false,
      addProductName: "",
      addProductCategory: "",
      addProductPrice: "",
      addProductDescription: "",
      addProductImage: "",
      categories: [], 
    };
  },
  mounted() {
    this.fetchProducts();
    this.fetchCategories();
  },
  methods: {
    fetchProducts() {
      apiClient
        .get("/products/")
        .then((response) => {
          this.products = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    fetchCategories() {
      apiClient
        .get("/productcategories/")
        .then((response) => {
          const categories = {};
          response.data.forEach((category) => {
            categories[category.category_id] = category.name;
          });
          this.categories = categories;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getCategoryLabel(category) {
      if (category in this.categories) {
        return this.categories[category];
      } else {
        return "";
      }
    },
    openImageDialog(image) {
      this.selectedImage = image;
      this.imageDialog = true;
    },
    closeImageDialog() {
      this.imageDialog = false;
    },
    openAddProductDialog() {
      this.addProductDialog = true;
    },
    closeAddProductDialog() {
      this.addProductDialog = false;
      this.addProductName = "";
      this.addProductCategory = "";
      this.addProductPrice = "";
      this.addProductDescription = "";
      this.addProductImage = "";
    },
    openAddCategoryDialog() {
      this.addCategoryDialog = true;
    },
    closeAddCategoryDialog() {
      this.addCategoryDialog = false;
      this.newCategoryName ="";
    },
    addCategory() {
      if (this.newCategoryName) {
        const data = {
          name: this.newCategoryName,
        };
        apiClient
          .post("/productcategories/", data)
          .then((response) => {
            this.fetchCategories();
            this.closeAddCategoryDialog();
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
  },
};
</script>

<style scoped>
</style>