<template>
  <div id="app">
    <div id="nav">
        <router-link :to="{ name: 'MovieList' }">Movies</router-link> |
      <span v-if="login">
        <router-link @click.native="logout" to="#">Logout</router-link>       
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link> 
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
      this.$store.state.is_admin = false
      this.$router.push({ name: 'Login' })
    }
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
  },
  computed : {
    ...mapState([
      'is_admin'
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
</style>
