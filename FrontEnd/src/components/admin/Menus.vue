<template>
  <v-app>
    <v-card fluid class="m-3">
      <v-card-title>
        <span class="fs-1">Menus</span>
        <v-btn color="primary" class="float-right" @click="openAddProductDialog"
          >Add Product</v-btn
        >
        <v-btn
          color="primary"
          class="float-right me-3"
          @click="openAddCategoryDialog"
          >Add Category</v-btn
        >
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
                <v-btn icon small @click="openEditProductDialog(item)">
                  <v-icon>mdi-pencil</v-icon>
                </v-btn>
              </td>
              <td>
                <v-btn icon small @click="openDeleteProductDialog(item)">
                  <v-icon> mdi-delete-forever </v-icon>
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
        <v-card-title> Add Product </v-card-title>
        <v-card-text>
          <v-form enctype="multipart/form-data" @submit.prevent="addProduct">
            <v-text-field
              v-model="newProduct.product_name"
              label="Product Name"
              :rules="[(v) => !!v || 'This field is required']"
              required
            ></v-text-field>
            <v-select
              v-model="newProduct.category"
              :items="rawCategories"
              item-title="name"
              item-value="category_id"
              label="Product Category"
              :rules="[(v) => !!v || 'This field is required']"
              required
            ></v-select>
            <v-text-field
              v-model.number="newProduct.price"
              type="number"
              label="Product Price"
              :rules="[(v) => !!v || 'This field is required']"
              required
            ></v-text-field>
            <v-textarea
              v-model="newProduct.product_detail"
              label="Product Description (optional)"
            ></v-textarea>
            <!-- Generate button -->
            <v-row justify="center" class="mb-4">
              <v-btn
                @click="generateGPTDescription"
                color="primary"
                class="mr-4"
              >
                <v-icon left>mdi-refresh</v-icon>
                Generate Description
              </v-btn>
            </v-row>
            <v-file-input
              v-model="newProduct.image"
              accept="image/*"
              label="Product Image (optional)"
              outlined
              prepend-icon="mdi-image"
              @change="handleImageUpload_add"
            ></v-file-input>
            <v-img v-if="newProduct.imageUrl" :src="newProduct.imageUrl" />
            <v-card-actions>
              <v-btn text @click="closeAddProductDialog">Cancel</v-btn>
              <v-btn type="submit" color="primary">Add</v-btn>
            </v-card-actions>
          </v-form>
        </v-card-text>
      </v-card>
    </v-dialog>
    <v-dialog v-model="editProductDialog" max-width="500px">
      <v-card>
        <v-card-title> Edit Product </v-card-title>
        <v-card-text>
          <v-form enctype="multipart/form-data" @submit.prevent="updateProduct">
            <v-text-field
              v-model="selectedProduct.product_name"
              label="Product Name"
              :rules="[(v) => !!v || 'This field is required']"
              required
            ></v-text-field>
            <v-select
              v-model="selectedProduct.category"
              :items="rawCategories"
              item-title="name"
              item-value="category_id"
              label="Product Category"
              :rules="[(v) => !!v || 'This field is required']"
              required
            ></v-select>
            <v-text-field
              v-model.number="selectedProduct.price"
              type="number"
              label="Product Price"
              :rules="[(v) => !!v || 'This field is required']"
              required
            ></v-text-field>
            <v-textarea
              v-model="selectedProduct.product_detail"
              label="Product Description (optional)"
            ></v-textarea>
            <v-file-input
              v-model="selectedProduct.image_new"
              accept="image/*"
              label="Product Image (optional)"
              outlined
              prepend-icon="mdi-image"
              @change="handleImageUpload_edit"
            ></v-file-input>
            <v-img v-if="selectedProduct.image" :src="selectedProduct.image" />
            <v-card-actions>
              <v-btn text @click="closeEditProductDialog">Cancel</v-btn>
              <v-btn type="submit" color="primary">Update</v-btn>
            </v-card-actions>
          </v-form>
        </v-card-text>
      </v-card>
    </v-dialog>

    <v-dialog v-model="deleteProductDialog" max-width="500px">
      <v-card>
        <v-card-title class="headline"
          >Delete product:&nbsp;{{ deleteProduct.name }}</v-card-title
        >
        <v-card-text>
          <span>Are you sure you want to delete {{ deleteProduct.name }}?</span>
        </v-card-text>
        <v-card-actions>
          <v-btn color="error" text @click="deleteMenuProduct">Confirm</v-btn>
          <v-btn text @click="closeDeleteProductDialog">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-app>
</template>

<script>
import apiClient from "@/axios/apiClient";
import { generateDescription } from "@/methods/gpt/generateDescription";

export default {
  name: "Menus",
  data() {
    return {
      products: [],
      categories: {},
      rawCategories: {},
      headers: [
        { title: "Product Name", value: "product_name", sortable: true },
        { title: "Category", value: "category", sortable: true },
        { title: "Price", value: "price", sortable: true },
        { title: "Description", value: "product_detail", sortable: true },
        { title: "Published Date", value: "pub_date", sortable: true },
        { title: "Image", value: "imageUrl", sortable: false },
        { title: "Edit", value: "edit", sortable: false },
        { title: "Delete", value: "delete", sortable: false },
      ],
      imageDialog: false,
      selectedImage: "",
      addCategoryDialog: false,
      newCategoryName: "",
      addProductDialog: false,
      editProductDialog: false,
      newProduct: {
        product_name: "",
        price: null,
        category: null,
        image: null,
        product_detail: "",
      },
      selectedProduct: {
        product_id: null,
        product_name: "",
        price: null,
        category: null,
        image: null,
        image_new: null,
        product_detail: "",
        imageUrl: "",
      },
      deleteProductDialog: false,
      deleteProduct: {
        id: "",
        name: "",
      },
      gptBtn:false,
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
          this.rawCategories = response.data;
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
      this.gptBtn = true;
    },
    closeAddProductDialog() {
      this.addProductDialog = false;
      this.newProduct.product_name = "";
      this.newProduct.price = null;
      this.newProduct.category = null;
      this.newProduct.product_detail = "";
      this.newProduct.image = null;

      this.gptBtn = true;
    },
    openAddCategoryDialog() {
      this.addCategoryDialog = true;
    },
    closeAddCategoryDialog() {
      this.addCategoryDialog = false;
      this.newCategoryName = "";
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
    addProduct() {
      console.log(this.newProduct);
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
          this.$toast.success(this.newProduct.product_name + " added", {
            duration: 6000,
          });
          this.fetchProducts();
          this.closeAddProductDialog();
        })
        .catch((error) => {
          console.error("Error creating product:", error);
        });
    },

    openEditProductDialog(product) {
      this.selectedProduct = { ...product };
      this.editProductDialog = true;
    },
    closeEditProductDialog() {
      this.editProductDialog = false;
      // this.selectedProduct = null;
    },
    updateProduct() {
      const { product_id } = this.selectedProduct;

      // Create a FormData object to send the updated product data as multipart/form-data
      const formData = new FormData();
      formData.append("product_name", this.selectedProduct.product_name);
      formData.append("price", this.selectedProduct.price);
      formData.append("category", this.selectedProduct.category);

      // Check if an image file is selected
      if (this.selectedProduct.image_new) {
        formData.append("image", this.selectedProduct.image_new);
      }

      formData.append("product_detail", this.selectedProduct.product_detail);

      apiClient
        .put(`/products/${product_id}/`, formData)
        .then((response) => {
          this.$toast.success(this.selectedProduct.product_name + " updated", {
            duration: 6000,
          });
          this.fetchProducts();
          this.closeEditProductDialog();
        })
        .catch((error) => {
          console.error("Error updating product:", error);
        });
    },

    handleImageUpload_edit(event) {
      const file = event.target.files[0];
      this.selectedProduct.image_new = file;

      // Read the file and display the image
      const reader = new FileReader();
      reader.onload = (e) => {
        this.selectedProduct.imageUrl = e.target.result;
      };
      reader.readAsDataURL(file);
    },

    openDeleteProductDialog(product) {
      this.deleteProduct.id = product.product_id;
      this.deleteProduct.name = product.product_name;

      this.deleteProductDialog = true;
    },
    closeDeleteProductDialog() {
      this.deleteProductDialog = false;
    },
    deleteMenuProduct() {
      apiClient
        .delete(`/products/${this.deleteProduct.id}/`)
        .then(() => {
          console.log("Product deleted successfully");
          // Refresh the product list
          this.fetchProducts();
          this.$toast.success(this.deleteProduct.name + " deleted", {
            duration: 6000,
          });
          this.deleteProduct.id = "";
          this.deleteProduct.name = "";
          this.deleteProductDialog = false;
        })
        .catch((error) => {
          console.error(error);
          // Handle error
        });
    },
    generateGPTDescription() {
      // Call the generateDescription function here
      if (!this.newProduct.product_name|| this.gptBtn == false){
        this.$toast.error("Product name is required to generate description.", {
            duration: 6000,
          });
        return;
      }
      generateDescription(this.newProduct.product_name)
        .then((description) => {
        this.gptBtn = false;
          // Do something with the generated description
          this.newProduct.product_detail = description;
          this.$toast.success("Description generated.", {
            duration: 6000,
          });
        })
        .catch((error) => {
        this.gptBtn = false;
          this.$toast.error(error, {
            duration: 6000,
          });
          // Handle the error appropriately (e.g., show an error message)
        });
    },
  },
};
</script>