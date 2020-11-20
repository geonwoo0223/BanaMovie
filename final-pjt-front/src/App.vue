<template>
  <div id="app">
    <div id="nav">
      <span v-if="login">
        <router-link @click.native="logout" to="#">Logout</router-link>       
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link> 
      </span>
    </div>
    <router-view @login="login = true"/>
  </div>
</template>

<script>

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
      this.$router.push({ name: 'Login' })
    }
  },
  created: function () {
    // 로그인
    const token = localStorage.getItem('jwt')

    if (token) {
      this.login = true
    }

    // DB
    // axios.get('https://api.themoviedb.org/3/movie/popular?api_key=e8067ff017c9f1acd66ea2924205aae6&language=ko-KR')
    //   .then( (res) => {
    //     // console.log(res.data.results)
    //     const movies = res.data.results
    //     const movieList = []
    //     for (const movie of movies) {
    //       // console.log(movie)
    //       const movieInfo = {
    //         title: movie.title,
    //         release_date: movie.release_date,
    //         poster_path: movie.poster_path,
    //         adult: movie.adult,
    //         overview: movie.overview,
    //         genres: movie.genre_ids
    //       }
    //       movieList.push(movieInfo)
    //     }
    //     console.log(movieList)
    //     axios.post('http://127.0.0.1:8000/movies/', movieList)
    //       .then( (res) => {
    //         console.log(res)
    //       })
    //       .catch( (err) => {
    //         console.log(err)
    //       })
    //   })
    //   .catch( (err) => {
    //     console.log(err)
    //   })
    axios.get('http://127.0.0.1:8000/movies/')
      .then( (res) => {
        console.log(res)
      })
      .catch( (err) => {
        console.log(err)
      })
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
