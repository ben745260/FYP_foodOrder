<template>
    <v-app>
      <v-container>
        <p>
          We value your opinion and feedback. Please let us know about your dining
          experience.
        </p>
  
        <v-form @submit="submitFeedback">
          <v-textarea
            v-model="feedback"
            label="Leave your feedback"
            outlined
            rows="5"
            multi-line
            required
          ></v-textarea>
  
          <v-btn
            class="w-100"
            type="submit"
            color="primary"
            :disabled="feedback === ''"
          >Submit</v-btn>
        <h3 class="mt-5">{{ response }}</h3>

        </v-form>
      </v-container>
    </v-app>
  </template>
  
  <script>
  import apiClient from "@/axios/apiClient";
  
  export default {
    name: "TableFeedback",
    data() {
      return {
        feedback: "",
        response: "",
      };
    },
    methods: {
      submitFeedback(event) {
        event.preventDefault(); // Prevent page refresh
  
        const data = {
          feedback_content: this.feedback,
        };
        apiClient
          .post("/feedbacks/", data)
          .then(() => {
            this.feedback = "";
            this.response = "Thank you for your feedback";
            this.$toast.success("Thank you for your feedback", {
              duration: 6000,
            });
          })
          .catch((error) => {
            // Handle the error case when creating the feedback
            console.error(error);
          });
      },
    },
  };
  </script>
  
  <style>
  </style>