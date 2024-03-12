<template>
  <div>
    <h1>Tables{{ table_id }}</h1>

    <!-- Button to add a new table -->
    <v-btn color="primary" @click="openAddTableDialog">Add Table</v-btn>

    <!-- Dialog for adding a new table -->
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

    <!-- Table list -->
    <v-data-table :items="tables" :headers="headers" item-key="tableId">
      <template #item="{ item }">
        <td>{{ item }}</td>
        <td>
          <v-btn color="primary" @click="navigateToTable(item)"
            >View Table</v-btn
          >
        </td>
      </template>
    </v-data-table>
  </div>
</template>
  
  <script>
export default {
  name: "Tables",
  data() {
    return {
      showAddTableDialog: false,
      newTableId: "",
      headers: [
        { text: "Table ID", value: "tableId" },
        { text: "Action", value: "action" },
      ],
      table_id: this.$store.state.tables,
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
        this.$store.commit("addTables", tableId);
        this.newTableId = "";
        this.showAddTableDialog = false;
      }
    },
    cancelAddTable() {
      this.showAddTableDialog = false;
      this.newTableId = "";
    },
    navigateToTable(tableId) {
      console.log(`Navigating to table ${tableId}`);
      this.$router.push(`/table/${tableId.tableId}`);
    },
  },
};
</script>
  
  <style scoped>
.v-data-table {
  margin-top: 16px;
}
</style>