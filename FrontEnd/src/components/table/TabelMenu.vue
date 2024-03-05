<template>
    <v-app>
        <v-row>
            <v-col cols="4">
                <v-card class="h-100" style="overflow-y: scroll;">
                    <v-list>
                        <v-list-item v-for="category in categories" :key="category.category_id" link
                            @click="scrollToCard(category.name)">
                            <v-list-item-content class="pl-0">
                                {{ category.name }}
                            </v-list-item-content>
                        </v-list-item>
                    </v-list>
                </v-card>
            </v-col>
            <v-col cols="8">
                <v-row>
                    <v-col v-for="category in categories" :key="category.category_id" cols="12" class="ps-1">
                        <v-card :id="category.name" variant="flat">
                            <v-card-title>{{ category.name }}</v-card-title>
                            <v-card-text>
                                <!-- Content of the card -->
                            </v-card-text>
                        </v-card>
                    </v-col>
                </v-row>
            </v-col>
        </v-row>
    </v-app>
</template>

<script>
import apiClient from '@/axios/apiClient';

export default {
    name: "TabelMenu",
    data() {
        return {
            drawer: false,
            categories: [],
        };
    },
    mounted() {
        this.fetchCategories();
    },
    methods: {
        fetchCategories() {
            apiClient
                .get('/productcategories/')
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
        scrollToCard(categoryName) {
            const cardElement = document.getElementById(categoryName);
            if (cardElement) {
                cardElement.scrollIntoView({ behavior: 'smooth' });
            }
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