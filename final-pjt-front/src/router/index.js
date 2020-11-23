import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import MovieList from '@/views/movies/MovieList'
import ManageMovie from '@/views/admin/ManageMovie'
import AdminManagement from '@/views/admin/AdminManagement'
import Board from '@/views/community/Board'
import CreateBoard from '@/views/community/CreateBoard'
import BoardDetail from '@/views/community/BoardDetail'


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
    path: '/managemovie',
    name: 'ManageMovie',
    component: ManageMovie,
  },
  {
    path: '/management',
    name: 'AdminManagement',
    component: AdminManagement,
  },
  {
    path: '/board',
    name: 'Board',
    component: Board,
  },
  {
    path: '/createboard',
    name: 'CreateBoard',
    component: CreateBoard,
  },
  {
    path: '/boarddetail',
    name: 'BoardDetail',
    component: BoardDetail,
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
