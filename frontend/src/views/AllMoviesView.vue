<template>
  <div class="container mt-5 mb-5">
    <h2 class="mb-4">All Movies</h2>

    <div v-if="movies.length" class="row">
      <div class="col-md-4 mb-4" v-for="movie in movies" :key="movie.id">
        <div class="card h-100 shadow-sm">
          <img
            :src="`/uploads/${movie.poster}`"
            class="card-img-top"
            :alt="movie.title"
          />
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
            <p class="card-text">{{ movie.description }}</p>
          </div>
        </div>
      </div>
    </div>

    <div v-else>
      <p>No movies found.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

let movies = ref([])

onMounted(() => {
  fetch('/api/v1/movies')
    .then((res) => res.json())
    .then((data) => {
      movies.value = data.movies
    })
})
</script>

<style>
/* Optional scoped styles */
.card-img-top {
  max-height: 300px;
  object-fit: cover;
}
</style>
