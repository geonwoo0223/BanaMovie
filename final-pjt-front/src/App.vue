<template>
  <div id="app">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
      integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">



    <div class="main-nav">


      <nav class="navbar navbar-expand-lg">
        <!-- <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText"
        aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button> -->
        <div class="collapse navbar-collapse" id="navbarText">
          <span v-if="login" class="navbar-text float-right">
              <router-link @click.native="logout" to="#" class="nav-margin">Logout</router-link>
          </span>

          <span else class="navbar-text float-right">
              <router-link :to="{ name: 'Signup' }" class="mr-auto nav-margin">Signup</router-link>
              <router-link :to="{ name: 'Login' }" class="mr-auto nav-margin "> <button
                  class="btn btn-primary">Login</button>
              </router-link>
          </span>
          <!-- <span class="navbar-text">
            Navbar text with an inline element
          </span> -->
        </div>
      </nav>

    </div>










    <div id="nav" class="p-2 main-nav">
      <b-navbar toggleable="lg" type="dark" id="navbar">
        <b-navbar-brand :style="{'font-size':'40px'}" class="nav-margin">
          <router-link :to="{ name: 'MovieList' }" id="logo">바나무비</router-link>
        </b-navbar-brand>


        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <router-link :to="{ name: 'MovieList' }" class="nav-margin">Movies</router-link>
            <router-link :to="{ name: 'Board' }" class="nav-margin">Board</router-link>
          </b-navbar-nav>
          <b-navbar-nav>
            <div v-if="is_admin" class="float-right">
              <router-link :to="{ name: 'AddMovie' }" class="nav-margin">영화추가</router-link>
              <router-link :to="{ name: 'AdminManagement' }" class="nav-margin">회원관리</router-link>
            </div>
            <div v-if="login" class="mr-auto">
              <router-link @click.native="logout" to="#" class="nav-margin">Logout</router-link>
            </div>
            <div v-else class="mr-auto">
              <router-link :to="{ name: 'Signup' }" class="mr-auto nav-margin">Signup</router-link>
              <router-link :to="{ name: 'Login' }" class="mr-auto nav-margin "> <button
                  class="btn btn-primary">Login</button>
              </router-link>

            </div>

          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>







    <router-view @login="login = true" />
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

      // axios.get(`${SERVER_URL}/movies/`)
      //   .then( (res) => {
      //     // console.log(res.data)
      //     this.$store.dispatch('getMovie', res.data)

      //   })
      //   .catch( (err) => {
      //     console.log(err)
      //   })

      // this.$router.push({name: 'MovieList'})
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

  /* .btn-primary {
    background-color: #7bc143 !important;
    border-color: #7bc143 !important;
    color: #FFF;
  } */
</style>