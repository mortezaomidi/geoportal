import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Organization from '../views/Organization.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/organization',
    name: 'Organization',
    component: Organization
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
