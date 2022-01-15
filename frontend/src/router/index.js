import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Organization from '../views/Organization.vue'
import CreateOrganization from '../components/organization/CreateOrganization.vue'
import UpdateOrganization from '../components/organization/UpdateOrganization.vue'

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
  {
    path: '/organization/create',
    name: 'CreateOrganization',
    component: CreateOrganization
  },
  {
    path: '/organization/update/:id',
    name: 'UpdateOrganization',
    component: UpdateOrganization
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
