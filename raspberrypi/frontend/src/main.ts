import { createApp } from 'vue'
import { createRouter, Router, createWebHistory } from 'vue-router'
import 'bootstrap'
import './styles/style.scss'
import App from './App.vue'
import Home from './pages/Home.vue'
import NotFound from './pages/NotFound.vue'
import Configurate from './pages/Configurate.vue'
import Measurements from './pages/Measurements.vue'

const router: Router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: Home},
        { path: '/configurate', component: Configurate},
        { path: '/measurements', component: Measurements },
        { path: '/:pathMatch(.*)*', component: NotFound}
    ]
})

createApp(App)
    .use(router)
    .mount('#app')