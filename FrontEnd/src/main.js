
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'


//toastr
import Toaster from "@meforma/vue-toaster";


const app = createApp(App)

app.use(router)
app.use(Toaster, {
    position: "top-right",
    duration: 3000,

})

app.mount('#app')
