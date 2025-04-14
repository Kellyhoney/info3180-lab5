import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import AddMovieFormView from '../views/AddMovieFormView.vue'
import AllMoviesView from '../views/AllMoviesView.vue' // ✅ Import the new view

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/movies/create',
      name: 'add-movie',
      component: AddMovieFormView
    },
    {
      path: '/movies',             
      name: 'movie-list',
      component: AllMoviesView
    }
  ]
})

export default router
