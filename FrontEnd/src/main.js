import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

import ToastPlugin from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-bootstrap.css';

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
    components,
    directives,
  })
  
const app = createApp(App);
app.use(vuetify);
app.use(ToastPlugin);
app.use(ElementPlus)
app.use(store);
app.use(router);
app.mount('#app');