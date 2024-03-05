<template>
  <v-layout class="rounded rounded-md">
    <v-app-bar title="Application bar"></v-app-bar>

    <v-navigation-drawer>
      <v-list>
        <v-list-item title="Navigation drawer"></v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main class="d-flex align-center justify-center" style="min-height: 300px;">
      Main Content
    </v-main>
  </v-layout>
</template>
<script lang="ts" setup>
import { ref } from 'vue'

const tabPosition = ref('left')
</script>
<style>
.demo-tabs>.el-tabs__content {
  padding: 32px;
  color: #6b778c;
  font-size: 32px;
  font-weight: 600;
}

.el-tabs--right .el-tabs__content,
.el-tabs--left .el-tabs__content {
  height: 100%;
}
</style>

<!-- <template>
  <div>
    <h1>Token: {{ token }}</h1>
  </div>
</template>
  
<script>
import { mapState } from 'vuex';

export default {
  computed: {
    ...mapState(['token']),
  },
};
</script>
  
<style>
/* Your styles here */
</style> -->