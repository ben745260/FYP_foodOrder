import { createRouter, createWebHistory } from 'vue-router';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import Admin from '../views/Admin.vue';
import Test from '../views/Test.vue';
import NotFound from '../views/NotFound.vue';
import Table_User from '../views/Table-User.vue';

import store from '@/store';

import Dashboard from '../components/admin/Dashboard.vue';
import Orders from '../components/admin/Orders.vue';
import Tables from '../components/admin/Tables.vue';
import Menus from '../components/admin/Menus.vue';
import Settings from '../components/admin/Settings.vue';
import UserFeedback from '../components/admin/UserFeedback.vue';
import Analysis from '../components/admin/Analysis.vue';

import Cart from '../components/table/Cart.vue';
import Item from '../components/table/Item.vue';
import TableMenu from '../components/table/TableMenu.vue';
import ViewOrder from '../components/table/ViewOrder.vue';
import Recommdenation from '../components/table/Recommdenation.vue';
import TableFeedback from '../components/table/TableFeedback.vue';


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
      path: '/admin',
      name: 'admin',
      component: Admin,
      meta: { requiresAuth: true },
      children: [
        {
          path: '',
          name: 'dashboard',
          component: Dashboard,
        },
        {
          path: 'dashboard',
          component: Dashboard,
        },
        {
          path: 'orders',
          component: Orders,
        },
        {
          path: 'tables',
          component: Tables,
        },
        {
          path: 'menus',
          component: Menus,
        },
        {
          path: 'settings',
          component: Settings,
        },
        {
          path: 'userFeedback',
          component: UserFeedback,
        },
        {
          path: 'analysis',
          component: Analysis,
        }
      ],
    },
    {
      path: '/table/:tables',
      meta: { requiresAuth: null },
      component: Table_User,
      beforeEnter: (to, from, next) => {
        const tableId = Number(to.params.tables);
        const tables = store.state.tables;

        if (tables.includes(tableId)) {
          next();
        } else {
          next('/404'); // Redirect to a 404 page or handle the invalid case as desired
        }
      },
      children: [
        {
          path: '',
          name: 'table',
          component: TableMenu,
        },
        {
          path: 'Cart',
          component: Cart,
        },
        {
          path: 'item',
          component: Item,
        },
        {
          path: 'tablemenu',
          component: TableMenu,
        },
        {
          path: 'vieworder',
          component: ViewOrder,
        },
        {
          path: 'recommdenation',
          component: Recommdenation,
        },
        {
          path: 'feedback',
          component: TableFeedback,
        },
      ],
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
      redirect: '/admin/dashboard',
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
  if (to.meta.requiresAuth === true && !store.state.isAuthenticated) {
    next('/login');
  } else if (to.meta.requiresAuth === false && store.state.isAuthenticated) {
    next('/');
  } else {
    next();
  }
});

// router.afterEach(() => {
//   const navbarToggler = document.querySelector('.navbar-toggler');
//   if (navbarToggler.getAttribute('aria-expanded') === 'true') {
//     navbarToggler.click();
//   }
// });

export default router;