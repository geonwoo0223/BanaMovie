<template>
  <div id="app">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">

    <div id="nav">
        <router-link :to="{ name: 'MovieList' }">Movies</router-link> |
        <router-link :to="{ name: 'Board' }">Board</router-link> |   
      <span v-if="login">
        <router-link @click.native="logout" to="#">Logout</router-link>     
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }"> <button class="btn btn-primary">Login</button>
        </router-link> 
      </span>
      <span v-if="is_admin">
        | <router-link :to="{ name: 'AddMovie' }">영화추가</router-link> |
        <router-link :to="{ name: 'AdminManagement' }">관리자</router-link> 
      </span>
      
    </div>
    <router-view @login="login = true" />
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL

import { mapState } from 'vuex'
import axios from 'axios'

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
      this.$router.push({ name: 'Login' })
    },
  },
  created: function () {
    // 로그인
    const token = localStorage.getItem('jwt')

    if (token) {
      this.login = true
    }

    axios.get(`${SERVER_URL}/movies/`)
      .then( (res) => {
        // console.log(res.data)
        this.$store.dispatch('getMovie', res.data)

      })
      .catch( (err) => {
        console.log(err)
      })

    // this.$router.push({name: 'MovieList'})
  },
  computed : {
    ...mapState([
      'is_admin',
    ])
  }
}
</script>

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.btn-primary {
    background-color: #7bc143 !important;
    border-color: #7bc143 !important;
    color: #FFF; }

</style>
