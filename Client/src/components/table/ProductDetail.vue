<template>
  <v-dialog
    v-model="dialogVisible"
    fullscreen
    hide-overlay
    transition="dialog-bottom-transition"
    persistent
  >
    <v-toolbar color="grey lighten-3">
      <v-btn @click="closeDialog">
        <i class="fa-solid fa-xmark fa-2xl"></i>
      </v-btn>
      <v-toolbar-title class="fs-3">
        {{ selectedProduct ? selectedProduct.product_name : "" }}
      </v-toolbar-title>
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
              width="100%"
              max-width="400px"
              max-height="200px"
            >
            </v-img>
            <div class="mt-4 fs-5">
              <strong>Desciption:</strong>
              <div
                v-html="selectedProduct ? selectedProduct.product_detail : ''"
              ></div>
            </div>
          </v-window-item>
          <v-window-item value="qna">
            <v-btn color="primary" class="w-100" @click="gptTimePOST()"
              >How long will the dish take?</v-btn
            >
            <v-spacer></v-spacer>
            <v-btn color="primary" class="w-100 mt-3" @click="gptContainPOST()"
              >What will be contained in the dish?</v-btn
            >
            <v-spacer></v-spacer>
            <v-btn color="primary" class="w-100 mt-3" @click="gptDangerPOST()"
              >What food hypersensitivity may it include?</v-btn
            >
            <v-card
              class="mt-3"
              style="height: 500px"
              color="blue-grey-lighten-4"
            >
              <v-card-text class="fs-5">
                {{ gptAnswer }}
              </v-card-text>
            </v-card>
          </v-window-item>
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
            size="x-small"
          >
            <v-icon class="mdi mdi-minus"></v-icon>
          </v-btn>
          <span class="badge text-bg-light fs-6 my-auto mx-2">{{
            quantity
          }}</span>
          <v-btn
            :variant="'elevated'"
            color="primary"
            @click="incrementQuantity"
            size="x-small"
          >
            <v-icon class="mdi mdi-plus"></v-icon>
          </v-btn>
        </div>
        <v-btn
          :variant="'outlined'"
          color="primary"
          @click="addToCart"
          rounded="xl"
          class="ms-1"
          :disabled="quantity === 0"
        >
          Add to Cart
        </v-btn>
      </v-toolbar>
    </v-footer>
  </v-dialog>
</template>

<script>
import { generateDescription } from "@/methods/gpt/generateDescription";

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
      gptAnswer: "",
      gptTime: null,
      gptContain: null,
      gptDanger: null,
    };
  },
  watch: {
    dialogVisible(value) {
      if (value) {
        this.activeTab = "detail"; // Reset active tab to 'detail'
        this.quantity = 0;
        this.gptAnswer = "";
        this.gptTime = null;
        this.gptContain = null;
        this.gptDanger = null;
      }
    },
  },
  methods: {
    closeDialog() {
      this.dialogVisible = false;
      this.gptAnswer = "";
      this.gptTime = null;
      this.gptContain = null;
      this.gptDanger = null;
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
    gptTimePOST() {
      if (this.gptTime != null) {
        this.gptAnswer = this.gptTime;
        return;
      }
      let systemMsg =
        "You are a restaurant staff who repling customer question";
      let userMsg =
        `How long will the dish possible take? :` +
        this.selectedProduct.product_name;
      let assisMsg = "It might take around ... minutes to prepare the dish";
      generateDescription(assisMsg, systemMsg, userMsg)
        .then((description) => {
          this.gptTime = description;
          this.gptAnswer = description;
          // console.log(description);
        })
        .catch((error) => {
          this.$toast.error(error, {
            duration: 6000,
          });
        });
    },
    gptContainPOST() {
      if (this.gptContain != null) {
        this.gptAnswer = this.gptContain;
        return;
      }
      let systemMsg =
        "You are a restaurant staff who repling customer question";
      let userMsg =
        `What will be contained in the dish? :` +
        this.selectedProduct.product_name;
      let assisMsg = "It contains...";
      generateDescription(assisMsg, systemMsg, userMsg)
        .then((description) => {
          this.gptContain = description;
          this.gptAnswer = description;
          // console.log(description);
        })
        .catch((error) => {
          this.$toast.error(error, {
            duration: 6000,
          });
        });
    },
    gptDangerPOST() {
      if (this.gptDanger != null) {
        this.gptAnswer = this.gptDanger;
        return;
      }
      let systemMsg =
        "You are a restaurant staff who repling customer question";
      let userMsg =
        `What general food hypersensitivity may it include? :` +
        this.selectedProduct.product_name;
      let assisMsg = "Potential food hypersensitivities may include are: ...";
      generateDescription(assisMsg, systemMsg, userMsg)
        .then((description) => {
          this.gptDanger = description;
          this.gptAnswer = description;
          // console.log(description);
        })
        .catch((error) => {
          this.$toast.error(error, {
            duration: 6000,
          });
        });
    },
  },
};
</script>

<style scoped>
.square-bg-color {
  background-color: white;
  border-radius: 0;
}
.v-img {
  max-height: 400px;
}
</style>