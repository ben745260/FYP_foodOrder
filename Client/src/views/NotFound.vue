<template>
  <v-container class="not-found-page" fluid>
    <v-row justify="center" :align="center" class="fill-height">
      <v-col cols="12" class="text-center">
        <h1 class="not-found-title">404 Not Found</h1>
        <p class="not-found-description">The page you are looking for does not exist.</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {

}
</script>

<style>
.not-found-page {
  background-color: #f5f5f5;
}

.not-found-title {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.not-found-description {
  font-size: 1rem;
  color: #888;
}
</style>