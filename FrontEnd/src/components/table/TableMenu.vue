<template>
  <v-app>
    <v-container class="pt-1 px-3">
      <v-row>
        <v-col
          v-for="category in categories"
          :key="category.category_id"
          cols="12"
          class="ps-1 pt-0"
        >
          <v-card :id="`card-${category.category_id}`" variant="flat">
            <v-card-title class="fs-4">{{ category.name }}</v-card-title>
            <v-card-text>
              <v-row
                v-for="product in getProductsByCategory(category.category_id)"
                @click="openDialog(product)"
                :key="product.product_id"
              >
                <v-col cols="4">
                  <v-img
                    :src="product.image"
                    :height="100"
                    class="rounded border border-primary"
                    alt="Product Image"
                  ></v-img>
                </v-col>
                <v-col cols="8">
                  <h3>{{ product.product_name }}</h3>
                  <h3 class="text-primary mt-5 pt-3">
                    ${{ product.price }}
                    <v-btn class="float-end fa-solid fa-plus"></v-btn>
                  </h3>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <dialog-component :selectedProduct="selectedProduct" ref="dialog"></dialog-component>
    <!-- </v-col>
    </v-row> -->
  </v-app>
</template>

<script>
import apiClient from "@/axios/apiClient";
import DialogComponent from "./ProductDetail.vue";

export default {
  name: "TableMenu",
  components: {
    DialogComponent,
  },
  data() {
    return {
      drawer: false,
      categories: [],
      products: [],
      selectedProduct: null, // Add selectedProduct property
    };
  },
  mounted() {
    this.fetchCategories();
    this.fetchProducts();
  },
  methods: {
    fetchCategories() {
      apiClient
        .get("/productcategories/")
        .then((response) => {
          const categories = response.data.map((category) => ({
            category_id: category.category_id,
            name: category.name,
            icon: category.icon,
          }));
          this.categories = categories;
        })
        .catch((error) => {
          console.error(error);
        });
    },
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
    getProductsByCategory(categoryId) {
      return this.products.filter((product) => product.category === categoryId);
    },
    openDialog(product) {
      this.selectedProduct = product;
      this.$refs.dialog.dialogVisible = true;
    },
  },
};
</script>

<style scoped>
/* .v-card{
        margin-bottom: 1;
    } */
.v-row {
  /* padding-left: 0; */
  padding-right: 0;
}

.v-col {
  /* padding-left: 0; */
  /* padding-right: 0; */
  /* padding-bottom: 0; */
}
</style>