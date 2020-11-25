<template>
  <div id="app">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
      integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">

    <div id="nav" class="p-2 main-nav">
      <b-navbar toggleable="lg" type="dark" id="navbar">
        <b-navbar-brand :style="{'font-size':'40px'}" class="nav-margin">
          <router-link :to="{ name: 'MovieList' }" id="logo" class="font-weight-bold">바나무비</router-link>
        </b-navbar-brand>


        <b-collapse id="nav-collapse" is-nav class="d-flex justify-content-between">

          <b-navbar-nav>
            <router-link :to="{ name: 'MovieList' }" class="nav-margin">Movies</router-link>
            <router-link :to="{ name: 'Board' }" class="nav-margin">Board</router-link>
          </b-navbar-nav>

          <b-navbar-nav>
            <div v-if="is_admin">
              <router-link :to="{ name: 'ManageMovie' }" class="nav-margin">영화관리</router-link>
              <router-link :to="{ name: 'AdminManagement' }" class="nav-margin">회원관리</router-link>
            </div>
            <div v-if="login" class="mr-auto">
              <router-link @click.native="logout" to="#" class="nav-margin">Logout</router-link>
            </div>
            <div v-else class="mr-auto">
              <router-link :to="{ name: 'Signup' }" class="mr-auto nav-margin"><button
                  class="btn btn-pink">Signup</button></router-link>
              <router-link :to="{ name: 'Login' }" class="mr-auto nav-margin "> <button
                  class="btn btn-pink">Login</button>
              </router-link>
            </div>
          </b-navbar-nav>

        </b-collapse>
      </b-navbar>
    </div>

    <router-view @login="login = true" />

    <div class="jumbotron">
      <div class="container">
        <h2 class="display-5">영화에 반하다, 바나무비</h2>
        <p class="lead">
          <a style="color:white; text-decoration:none" href="https://github.com/snowcuphea">김민정</a> &
          <a style="color:white; text-decoration:none" href="https://github.com/geonwoo0223">이건우</a>        
        </p>
        <p>Copyright © 2020 TEAM DEJAVUE. ALL RIGHTS RESERVED</p>
        <p class="lead">
          <a class="btn btn-dark" href="https://www.themoviedb.org/?language=ko" role="button">TMBD</a>
        </p>

      </div>
    </div>





  </div>
</template>

<script>
  // const SERVER_URL = process.env.VUE_APP_SERVER_URL

  import {
    mapState
  } from 'vuex'
  // import axios from 'axios'

  export default {
    name: 'App',
    data: function () {
      return {
        login: false,
      }
    },
    methods: {
      logout: function () {
        localStorage.removeItem('jwt')
        this.login = false
        this.$store.state.login = false
        this.$store.state.is_admin = false
        this.$store.state.login_user = ''
        this.$router.push({
          name: 'Login'
        })
      },
    },
    created: function () {
      // 로그인
      const token = localStorage.getItem('jwt')

      if (token) {
        this.login = true
      }
      this.$store.dispatch('getMovie')

    },
    computed: {
      ...mapState([
        'is_admin',
      ])
    }
  }
</script>
<!-- Js Plugins -->


<style>
  @import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&family=Jua&family=Nanum+Gothic&family=Poor+Story&family=Slabo+27px&display=swap');
  @import './assets/css/mycss.css';

  #app {
    font-family: 'Salbo 27px', 'Nanum Gothic', Helvetica, Arial, sans-serif;
    /* Do Hyeon Jua Poor Story */
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: white;
    background-color: #0B0C2A;
    width: 100%;
    min-height: 100vh;
  }
  
  #navbar {
    background-color: #070720;
  }

  #nav a {
    font-weight: bold;
    color: #2c3e50;
  }

  #nav a.router-link-exact-active {
    /* color: #D44C7F; */
    color: #DE5078;
  }

  #logo {
    color: #DE5078 !important;
  }

 
</style>