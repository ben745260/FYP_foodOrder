import { createRouter, createWebHistory } from 'vue-router'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import DashBoard from '../components/DashBoard.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashBoard
    },
    
  ]
})

export default router
