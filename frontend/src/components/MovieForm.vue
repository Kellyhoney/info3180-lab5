<template>
  <div class="container mt-5">
    <h2>Add a Movie</h2>

    <div v-if="errors.length" class="alert alert-danger">
      <ul>
        <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
      </ul>
    </div>

    <div v-if="successMessage" class="alert alert-success">
      {{ successMessage }}
    </div>

    <form @submit.prevent="saveMovie" id="movieForm">
      <div class="form-group mb-3">
        <label for="title">Movie Title</label>
        <input type="text" name="title" class="form-control" />
      </div>

      <div class="form-group mb-3">
        <label for="description">Description</label>
        <textarea name="description" class="form-control"></textarea>
      </div>

      <div class="form-group mb-3">
        <label for="poster">Movie Poster</label>
        <input type="file" name="poster" class="form-control" />
      </div>

      <button type="submit" class="btn btn-primary">Submit Movie</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"

let csrf_token = ref("")
let errors = ref([])
let successMessage = ref("")

function getCsrfToken() {
  fetch("http://localhost:8080/api/v1/csrf-token")
    .then((res) => res.json())
    .then((data) => {
      csrf_token.value = data.csrf_token
    })
    .catch((error) => {
      console.error("Failed to get CSRF token:", error)
    })
}

function saveMovie() {
  errors.value = []
  successMessage.value = ""

  let movieForm = document.getElementById("movieForm")
  let form_data = new FormData(movieForm)

  fetch("http://localhost:8080/api/v1/movies", {
    method: "POST",
    body: form_data,
    headers: {
      "X-CSRFToken": csrf_token.value,
    },
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.errors) {
        errors.value = data.errors
      } else {
        successMessage.value = data.message
        movieForm.reset()
      }
    })
    .catch((error) => {
      console.error("Error submitting movie:", error)
    })
}

onMounted(() => {
  getCsrfToken()
})
</script>
