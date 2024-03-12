<template>
  <v-app>
    <v-card fluid class="m-3">
      <v-card-title>
        <span class="fs-1">Menus</span>
        <v-btn color="primary" class="float-right">Add Product</v-btn>
        <v-btn color="primary" class="float-right me-3">Add Category</v-btn>
      </v-card-title>
      <v-card-text>
        <v-data-table
          :headers="headers"
          :items="filteredProducts"
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
                <v-btn icon small @click="openImageDialog(item.image)">
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
        <v-card-title>
          Image
        </v-card-title>
        <v-card-text>
          <v-img :src="selectedImage" contain></v-img>
        </v-card-text>
        <v-card-actions>
          <v-btn text @click="closeImageDialog">Close</v-btn>
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
      search: "",
      filteredProducts: [],
      imageDialog: false,
      selectedImage: "",
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
          this.filteredProducts = this.products; // Initialize filteredProducts with all products
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
      this.selectedImage = "";
    },
  },
};
</script>