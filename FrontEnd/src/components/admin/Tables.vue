<template>
  <v-app>
    <v-card fluid class="m-3">
      <v-card-title>
        <span class="fs-1">Tables </span>
        <v-btn color="primary" @click="openAddTableDialog" class="float-right"
          >Add Table</v-btn
        >
      </v-card-title>
      <v-card-text>
        <v-data-table :items="tables" :headers="headers" item-key="tableId">
          <template #item="{ item }">
            <tr>
              <td>{{ item.tableId }}</td>
              <td>
                <v-btn color="primary" @click="navigateToTable(item.tableId)"
                  >View Table</v-btn
                >
              </td>
              <td>
                <v-btn color="primary" @click="showQRCodeDialog(item.tableId)"
                  >Show QR Code</v-btn
                >
              </td>
              <td>
                <v-btn color="primary" @click="showCheckoutDialog(item.tableId)"
                  >Checkout</v-btn
                >
              </td>
              <td>
                <v-btn color="error" @click="confirmRemoveTable(item.tableId)"
                  >Remove Table</v-btn
                >
              </td>
            </tr>
          </template>
        </v-data-table>
      </v-card-text>
    </v-card>

    <!-- Dialogs -->
    <v-dialog v-model="isAddTableDialogVisible" persistent class="w-50">
      <v-card>
        <v-card-title>Add Table</v-card-title>
        <v-card-text>
          <v-text-field
            v-model="newTableId"
            label="Table ID"
            type="number"
          ></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" @click="addTable">Add</v-btn>
          <v-btn @click="cancelAddTable">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="isConfirmRemoveDialogVisible" persistent class="w-50">
      <v-card>
        <v-card-title>Confirm Removal</v-card-title>
        <v-card-text>Are you sure you want to remove the table?</v-card-text>
        <v-card-actions>
          <v-btn color="error" @click="removeTable">Remove</v-btn>
          <v-btn @click="cancelRemoveTable">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="isQRCodeDialogVisible" persistent class="w-50">
      <v-card>
        <v-card-title>Table {{ currentTableId }} QR Code</v-card-title>
        <v-card-text>
          <qrcode-vue
            :value="getViewTableUrl(currentTableId)"
            :size="200"
            level="H"
            class="d-flex mx-auto"
          />
        </v-card-text>
        <v-card-actions>
          <v-btn @click="closeQRCodeDialog">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Dialogs -->

    <v-dialog v-model="isCheckoutDialogVisible" persistent class="w-50">
      <v-card>
        <v-card-title>Table {{ currentTableId }} Checkout</v-card-title>
        <v-card-text>
          <p class="fw-bold">Total Amount:{{ tableTotalAmount }}</p>
          Are you sure you want to checkout Table {{ currentTableId }}?
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" @click="confirmCheckout">Confirm</v-btn>
          <v-btn color="" @click="closeCheckoutDialog">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-app>
</template>
  
<script>
import QrcodeVue from "qrcode.vue";
import apiClient from "@/axios/apiClient";

export default {
  name: "Tables",
  data() {
    return {
      isAddTableDialogVisible: false,
      isConfirmRemoveDialogVisible: false,
      isQRCodeDialogVisible: false,
      newTableId: "",
      headers: [
        { title: "Table ID", align: "start", value: "tableId", sortable: true },
        { title: "Action", align: "start", value: "action" },
        { title: "QR Code", align: "start", value: "action" },
        { title: "Checkout", align: "start", value: "action" },
        { title: "Remove", align: "start", value: "remove" },
      ],
      tableToRemove: null,
      currentTableId: null,
      isCheckoutDialogVisible: false,
      tableTotalAmount: "",
    };
  },
  computed: {
    tables() {
      return this.$store.state.tables.map((tableId) => ({ tableId }));
    },
  },
  components: {
    QrcodeVue,
  },
  methods: {
    openAddTableDialog() {
      this.isAddTableDialogVisible = true;
    },
    addTable() {
      const tableId = parseInt(this.newTableId);
      if (!isNaN(tableId)) {
        const existingTable = this.tables.find(
          (table) => table.tableId === tableId
        );
        if (!existingTable) {
          this.$store.commit("addTables", tableId);
          this.newTableId = "";
          this.isAddTableDialogVisible = false;
        } else {
          alert("Table ID already exists.");
        }
      }
    },
    cancelAddTable() {
      this.isAddTableDialogVisible = false;
      this.newTableId = "";
    },
    navigateToTable(tableId) {
      console.log(`Navigating to table ${tableId}`);
      this.$router.push(`/table/${tableId}/tablemenu`);
    },
    confirmRemoveTable(tableId) {
      this.tableToRemove = tableId;
      this.isConfirmRemoveDialogVisible = true;
    },
    removeTable() {
      this.$store.commit("removeTable", this.tableToRemove);
      this.isConfirmRemoveDialogVisible = false;
      this.tableToRemove = null;
    },
    cancelRemoveTable() {
      this.isConfirmRemoveDialogVisible = false;
      this.tableToRemove = null;
    },
    showQRCodeDialog(tableId) {
      this.currentTableId = tableId;
      this.isQRCodeDialogVisible = true;
    },
    closeQRCodeDialog() {
      this.isQRCodeDialogVisible = false;
      this.currentTableId = null;
    },
    getViewTableUrl(tableId) {
      return `http://localhost:5173/table/${tableId}/tablemenu`;
    },

    showCheckoutDialog(tableId) {
      this.currentTableId = tableId;
      this.isCheckoutDialogVisible = true;

      // Make an API request to retrieve the orders
      apiClient
        .get(`/orders/table/${tableId}/`)
        .then((response) => {
          const orders = response.data;
          const totalAmount = orders.reduce((sum, order) => {
            if (!order.order_checkout) {
              return sum + parseFloat(order.order_amount);
            }
            return sum;
          }, 0);
          this.tableTotalAmount = totalAmount;
          console.log("Total amount:", totalAmount);
        })
        .catch((error) => {
          console.error("Failed to retrieve orders", error);
        });
    },
    closeCheckoutDialog() {
      this.isCheckoutDialogVisible = false;
      this.currentTableId = null;
      this.tableTotalAmount = "";
    },
    confirmCheckout() {
      // Make an API request to update the order
      const payload = {
        order_checkout: true,
      };
      apiClient
        .put(`/orders/table/${this.currentTableId}/`, payload)
        .then((response) => {
          // Handle the response if needed
          this.$toast.success(
            `Table ${this.currentTableId} Order checkout successful`,
            {
              duration: 6000,
            }
          );
          this.tableTotalAmount = "";
        })
        .catch((error) => {
          // Handle the error if needed
          console.error("Order checkout failed", error);
        });

      this.isCheckoutDialogVisible = false;
      this.currentTableId = null;
    },
  },
};
</script>
  
  <style>
/* Add your custom styles here */
</style>