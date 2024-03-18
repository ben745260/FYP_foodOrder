<template>
    <v-app>
      <v-card fluid class="m-3">
        <v-card-title>
          <span class="fs-1">User Feedback</span>
          <v-btn color="primary" class="float-right">Feedback analysis</v-btn>
        </v-card-title>
        <v-card-text>
          <v-data-table :items="feedbacks" :headers="headers" item-key="feedbackId">
            <template #item="{ item }">
              <tr>
                <td>{{ item.feedback_id }}</td>
                <td>{{ item.feedback_dateTime }}</td>
                <td>{{ item.feedback_content }}</td>
              </tr>
            </template>
          </v-data-table>
        </v-card-text>
      </v-card>
    </v-app>
  </template>
  
  <script>
  import apiClient from "@/axios/apiClient";
  
  export default {
    name: "UserFeedback",
    data() {
      return {
        headers: [
          { title: "ID", align: "start", value: "feedbackId", sortable: true },
          {
            title: "Submit Time",
            align: "start",
            value: "submitTime",
            sortable: true,
          },
          { title: "Content", align: "start", value: "content" },
        ],
        feedbacks: [],
      };
    },
    mounted() {
      this.fetchFeedbacks();
    },
    methods: {
      fetchFeedbacks() {
        apiClient
          .get("/feedbacks/")
          .then((response) => {
            this.feedbacks = response.data;
          })
          .catch((error) => {
            console.error(error);
          });
      },
    },
  };
  </script>
  
  <style>
  </style>