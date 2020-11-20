import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import MovieList from '@/views/movies/MovieList'
import MovieDetail from '@/views/movies/MovieDetail'
import AddMovie from '@/views/admin/AddMovie'
import AdminManagement from '@/views/admin/AdminManagement'


Vue.use(VueRouter)

const routes = [
  
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/movies',
    name: 'MovieList',
    component: MovieList,
  },
  {
    path: '/movie',
    name: 'MovieDetail',
    component: MovieDetail,
  },
  {
    path: '/addmovie',
    name: 'AddMovie',
    component: AddMovie,
  },
  {
    path: '/management',
    name: 'AdminManagement',
    component: AdminManagement,
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
