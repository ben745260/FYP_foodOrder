import { createRouter, createWebHistory } from 'vue-router';
import Login from '../components/Login.vue';
import Register from '../components/Register.vue';
import DashBoard from '../components/DashBoard.vue';
import Test from '../components/Test.vue';
import NotFound from '../components/NotFound.vue';
import store from '@/store';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: { requiresAuth: false },
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
      meta: { requiresAuth: false },
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashBoard,
      meta: { requiresAuth: true },
    },
    {
      path: '/test',
      name: 'test',
      component: Test,
      meta: { requiresAuth: true },
    },
    {
      path: '/404',
      name: '404',
      component: NotFound,
    },
    {
      path: '/:catchAll(.*)',
      redirect: '/404',
    },
    {
      path: '/',
      redirect: '/dashboard',
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      // If the browser restored the previous scroll position, use it
      return savedPosition;
    } else {
      // Otherwise, scroll to the top of the page smoothly
      return new Promise((resolve) => {
        setTimeout(() => {
          window.scrollTo({
            top: 0,
            behavior: 'smooth',
          });
          resolve();
        }, 0);
      });
    }
  },
});

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !store.state.isAuthenticated) {
    next('/login');
  } else if (!to.meta.requiresAuth && store.state.isAuthenticated) {
    next('/');
  } else {
    next();
  }
});

router.afterEach(() => {
  const navbarToggler = document.querySelector('.navbar-toggler');
  if (navbarToggler.getAttribute('aria-expanded') === 'true') {
    navbarToggler.click();
  }
});

export default router;