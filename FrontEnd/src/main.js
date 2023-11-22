import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

import ToastPlugin from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-bootstrap.css';

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const app = createApp(App);
app.use(ToastPlugin);
app.use(ElementPlus)
app.use(store);
app.use(router);
app.mount('#app');