<template>
    <v-app>
      <v-card fluid class="m-3">
        <v-card-title>
          <span class="fs-1">Tables  </span>
          <v-btn color="primary" @click="openAddTableDialog" class="float-right">Add Table</v-btn>
        </v-card-title>
        <v-card-text>
          <v-data-table :items="tables" :headers="headers" item-key="tableId">
            <template #item="{ item }">
              <tr>
                <td>{{ item.tableId }}</td>
                <td>
                  <v-btn color="primary" @click="navigateToTable(item.tableId)">View Table</v-btn>
                </td>
                <td>
                  <v-btn color="error" @click="confirmRemoveTable(item.tableId)">Remove Table</v-btn>
                </td>
              </tr>
            </template>
          </v-data-table>
        </v-card-text>
      </v-card>
  
      <!-- Dialogs -->
      <v-dialog v-model="showAddTableDialog" persistent>
        <v-card>
          <v-card-title>Add Table</v-card-title>
          <v-card-text>
            <v-text-field v-model="newTableId" label="Table ID"></v-text-field>
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" @click="addTable">Add</v-btn>
            <v-btn @click="cancelAddTable">Cancel</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
  
      <v-dialog v-model="showConfirmRemoveDialog" persistent>
        <v-card>
          <v-card-title>Confirm Removal</v-card-title>
          <v-card-text>Are you sure you want to remove the table?</v-card-text>
          <v-card-actions>
            <v-btn color="error" @click="removeTable">Remove</v-btn>
            <v-btn @click="cancelRemoveTable">Cancel</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-app>
  </template>
  
  <script>
  export default {
    name: "Tables",
    data() {
      return {
        showAddTableDialog: false,
        showConfirmRemoveDialog: false,
        newTableId: "",
        headers: [
          { title: "Table ID", align: "start", value: "tableId", sortable: true },
          { title: "Action", align: "start", value: "action" },
          { title: "Remove", align: "start", value: "remove" },
        ],
        tableToRemove: null,
      };
    },
    computed: {
      tables() {
        return this.$store.state.tables.map((tableId) => ({ tableId }));
      },
    },
    methods: {
      openAddTableDialog() {
        this.showAddTableDialog = true;
      },
      addTable() {
        const tableId = parseInt(this.newTableId);
        if (!isNaN(tableId)) {
          const existingTable = this.tables.find((table) => table.tableId === tableId);
          if (!existingTable) {
            this.$store.commit("addTables", tableId);
            this.newTableId = "";
            this.showAddTableDialog = false;
          } else {
            alert("Table ID already exists.");
          }
        }
      },
      cancelAddTable() {
        this.showAddTableDialog = false;
        this.newTableId = "";
      },
      navigateToTable(tableId) {
        console.log(`Navigating to table ${tableId}`);
        this.$router.push(`/table/${tableId}/tablemenu`);
      },
      confirmRemoveTable(tableId) {
        this.tableToRemove = tableId;
        this.showConfirmRemoveDialog = true;
      },
      removeTable() {
        this.$store.commit("removeTable", this.tableToRemove);
        this.cancelRemoveTable();
      },
      cancelRemoveTable() {
        this.showConfirmRemoveDialog = false;
        this.tableToRemove = null;
      },
    },
  };
  </script>
  
  <style scoped>
  .v-data-table {
    margin-top: 16px;
  }
  </style>