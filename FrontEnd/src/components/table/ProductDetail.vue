<template>
  <v-dialog
    v-model="dialogVisible"
    fullscreen
    hide-overlay
    transition="dialog-bottom-transition"
  >
    <v-toolbar color="grey lighten-3">
      <v-btn @click="closeDialog"
        ><i class="fa-solid fa-xmark fa-2xl"></i
      ></v-btn>
      <v-toolbar-title class="fs-3">{{
        selectedProduct ? selectedProduct.product_name : ""
      }}</v-toolbar-title>
    </v-toolbar>
    <v-card>
      <v-card-title class="p-0">
        <v-tabs v-model="activeTab" background-color="transparent" grow>
          <v-tab value="detail">Detail</v-tab>
          <v-tab value="qna">QnA</v-tab>
        </v-tabs>
      </v-card-title>
      <v-card-text>
        <v-window v-model="activeTab">
          <v-window-item value="detail">
            <v-img
              :src="selectedProduct ? selectedProduct.image : ''"
              class="rounded border border-2 border-danger"
            />
            <div class="mt-4 fs-5">
              <strong>Desciption:</strong>
              <div
                v-html="selectedProduct ? selectedProduct.product_detail : ''"
              ></div>
            </div>
          </v-window-item>
          <v-window-item value="qna"> This is the QnA tab. </v-window-item>
        </v-window>
      </v-card-text>
    </v-card>
    <v-footer class="p-0" app>
      <v-toolbar dark>
        <v-toolbar-title class="fs-4 fw-bold ps-3">
          ${{ selectedProduct ? selectedProduct.price : "" }}
        </v-toolbar-title>
        <div class="mx-auto">
          <v-btn
            :variant="'elevated'"
            color="primary"
            @click="decrementQuantity"
            size="small"
          >
            <v-icon>fa-solid fa-minus</v-icon>
          </v-btn>
          <span class="badge text-bg-light fs-6 my-auto mx-2">{{
            quantity
          }}</span>
          <v-btn
            :variant="'elevated'"
            color="primary"
            @click="incrementQuantity"
            size="small"
          >
            <v-icon>fa-solid fa-plus</v-icon>
          </v-btn>
        </div>
        <v-btn
          :variant="'outlined'"
          color="primary"
          @click="addToCart"
          rounded="xl"
          class="ms-1"
        >
          Add to Cart
        </v-btn>
      </v-toolbar>
    </v-footer>
  </v-dialog>
</template>
  
  <script>
export default {
  name: "DialogComponent",
  props: {
    selectedProduct: {
      type: Object,
      default: null,
    },
  },
  data() {
    return {
      dialogVisible: false,
      quantity: 0,
      activeTab: "detail", // Set the default active tab to 'detail'
    };
  },
  watch: {
    dialogVisible(value) {
      if (value) {
        this.activeTab = "detail"; // Reset active tab to 'detail'
        this.quantity = 0;
      }
    },
  },
  methods: {
    closeDialog() {
      this.dialogVisible = false;
    },
    incrementQuantity() {
      this.quantity++;
    },
    decrementQuantity() {
      if (this.quantity > 0) {
        this.quantity--;
      }
    },
    addToCart() {
      // Check if the selectedProduct and quantity are valid
      if (this.selectedProduct && this.quantity > 0) {
        // Get the existing cart items from the local storage
        this.$store.commit("addToCart", {
          productId: this.selectedProduct.product_id,
          quantity: this.quantity,
          price: this.selectedProduct.price,
        });
      }
      // Close the dialog
      this.closeDialog();
    },
  },
};
</script>
  
  <style scoped>
.square-bg-color {
  background-color: white;
  border-radius: 0;
}
.v-img{
  max-height: 400px;
}
</style>