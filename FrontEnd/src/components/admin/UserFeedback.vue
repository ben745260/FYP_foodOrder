<template>
  <v-app>
    <v-card fluid class="m-3">
      <v-card-title>
        <span class="fs-1">User Feedback</span>
        <v-btn
          color="primary"
          class="float-right"
          @click="openDialog()"
          :disabled="!feedbacks"
          >Feedback analysis</v-btn
        >
      </v-card-title>
      <v-card-text>
        <v-data-table
          :items="feedbacks.slice().reverse()"
          :headers="headers"
          item-key="feedbackId"
        >
          <template #item="{ item }">
            <tr>
              <td>{{ item.feedback_id }}</td>
              <td>{{ formatDate(item.feedback_dateTime) }}</td>
              <td>{{ item.feedback_content }}</td>
            </tr>
          </template>
        </v-data-table>
      </v-card-text>
    </v-card>

    <v-dialog v-model="dialog" max-width="500px" persistent>
      <v-card>
        <!-- <v-card-title class="headline">Feedback Analysis</v-card-title>
        <v-divider></v-divider> -->
        <v-card-text>
          <div v-if="gptSumup !== 'Loading'">
            <div class="mb-4">
              <h3 class="subtitle-1">Summarized Feedback:</h3>
              <p>{{ gptSumup }}</p>
            </div>
            <div>
              <h3 class="subtitle-1">Suggestions:</h3>
              <p>{{ gptResult }}</p>
            </div>
          </div>
          <div v-else>
            <v-skeleton-loader
              type="text"
              :loading="true"
              class="mb-4"
            ></v-skeleton-loader>
            <v-skeleton-loader type="text" :loading="true"></v-skeleton-loader>
          </div>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn color="primary" text @click="dialog = false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-app>
</template>

<script>
import apiClient from "@/axios/apiClient";
import dayjs from "dayjs";
import { generateDescription } from "@/methods/gpt/generateDescription";

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
      sumFeedback: "",
      gptSumup: "Loading",
      gptResult: null,
      dialog: false,
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
          this.sumFeedback = this.feedbacks.reduce((acc, feedback) => {
            return acc + feedback.feedback_content + ",";
          }, "");
          // console.log(this.sumFeedback);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    formatDate(dateTime) {
      return dayjs(dateTime).format("HH:mm:ss, YYYY-MM-DD");
    },
    openDialog() {
      this.dialog = true;
      if (this.gptSumup != "Loading") {
        return;
      }
      let systemMsg =
        "You are a restaurant admin. You are reviewing the customer feedback to see how to improve your business";
      let userMsg =
        `These are the feedback from the customer with comma separated. summarize it. No suggestions needed (under 100 words):` +
        this.sumFeedback;
      let assisMsg = "";
      generateDescription(assisMsg, systemMsg, userMsg)
        .then((description) => {
          this.gptSumup = description;
          // console.log(description);
        })
        .catch((error) => {
          this.$toast.error(error, {
            duration: 6000,
          });
        });
      systemMsg =
        "You are a restaurant admin. You are reviewing the customer feedback to see how to improve your business";
      userMsg =
        `These are the summarized feedback from the customer with comma separated. Dont summarized it and Provide at least 3 suggestions with numbering (under 100 words):` +
        this.gptSumup;
      assisMsg = "";
      generateDescription(assisMsg, systemMsg, userMsg)
        .then((description) => {
          this.gptResult = description;
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

<style>
</style>