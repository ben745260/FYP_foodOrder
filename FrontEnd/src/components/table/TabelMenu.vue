<template>
  <v-app>
    <!-- <v-row>
      <v-col cols="4" class="py-0">
        <v-card class="h-100 w-25" style="position: fixed">
          <v-list>
            <v-list-item
              v-for="category in categories"
              :key="category.category_id"
              link
              @click="scrollToCard(category.category_id)"
            >
              <v-list-item-content class="pl-0">
                {{ category.name }}
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-card>
      </v-col>
      <v-col cols="8" class="py-0 ps-0"> -->
    <v-container class="pt-0 ps-1">
      <v-row>
        <v-col
          v-for="category in categories"
          :key="category.category_id"
          cols="12"
          class="ps-1 pt-0"
        >
          <v-card :id="`card-${category.category_id}`" variant="flat">
            <v-card-title>{{ category.name }} </v-card-title>
            <v-card-text>
              <v-row
                v-for="product in getProductsByCategory(category.category_id)"
                :key="product.product_id"
              >
                <v-col cols="4">
                  <v-img
                    :src="product.image"
                    :height="100"
                    class="round-sm border border-primary"
                    alt="Product Image"
                  ></v-img>
                </v-col>
                <v-col cols="6">
                  <h4>{{ product.product_name }}</h4>
                  <p>${{ product.price }}</p>
                </v-col>
                <v-col cols="2"></v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <!-- </v-col>
    </v-row> -->
  </v-app>
</template>
  
  <script>
import apiClient from "@/axios/apiClient";

export default {
  name: "TabelMenu",
  data() {
    return {
      drawer: false,
      categories: [],
      products: [],
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
  padding-right: 0;
  padding-bottom: 0;
}
</style>