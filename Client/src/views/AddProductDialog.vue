<template>
  <div>
    <v-btn color="primary" class="float-right" @click="openDialog"
      >Add Product</v-btn
    >
    <v-dialog v-model="dialogVisible" max-width="500px" persistent>
      <v-card>
        <v-card-title> Add Product{{ categories }} </v-card-title>
        <v-card-text>
          <!-- Add your form fields here -->
          <v-text-field
            v-model="productName"
            label="Product Name"
          ></v-text-field>
          <v-select
            v-model="productCategory"
            :items="categories"
            label="Product Category"
          ></v-select>
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
        <v-card-actions
          ><v-btn color="primary" @click="addProduct">Add</v-btn>
          <v-spacer></v-spacer>
          <v-btn text @click="closeDialog">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
  
<script>
import apiClient from "@/axios/apiClient";

export default {
  data() {
    return {
      dialogVisible: false,
      productName: "",
      productCategory: "",
      productPrice: "",
      productDescription: "",
      productImage: "",
      categories: [],
    };
  },
  methods: {
    fetchCategories() {
      apiClient
        .get("/productcategories/")
        .then((response) => {
          const categories = {};
          response.data.forEach((category) => {
            categories[category.category_id] = category.name;
          });
          this.categories = categories;
          console.log("here");
          console.log(this.categories);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    openDialog() {
      this.fetchCategories();
      this.dialogVisible = true;
    },
    closeDialog() {
      this.dialogVisible = false;
      this.resetForm();
    },

    resetForm() {
      this.productName = "";
      this.productCategory = "";
      this.productPrice = "";
      this.productDescription = "";
      this.productImage = "";
      // Reset other form fields as needed
    },
    addProduct() {
      // Perform validation on form fields
      if (
        this.productName.trim() === "" ||
        this.productCategory.trim() === "" ||
        this.productPrice.trim() === "" ||
        this.productDescription.trim() === "" ||
        this.productImage.trim() === ""
      ) {
        // Show an error message or handle the empty fields case
        return;
      }

      // Make a POST request to add the new product
      apiClient
        .post("/products/", {
          product_name: this.productName,
          category: this.productCategory,
          price: this.productPrice,
          description: this.productDescription,
          image: this.productImage,
          // Include other form field values in the request payload
        })
        .then((response) => {
          // Product successfully added, perform any necessary actions
          this.closeDialog(); // Close the dialog and reset the form
          // Perform any additional logic, such as refreshing the product list
          this.$emit("productAdded"); // Emit an event to notify the parent component
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>