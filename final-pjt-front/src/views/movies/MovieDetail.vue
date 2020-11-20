<template>
  <div>
    <h1>Title: {{ movie.title }}</h1>
    <h3>Overview: {{ movie.overview}}</h3>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL

import axios from 'axios'


export default {
  name: 'MovieDetail',
  data: function () {
    return {
      movie: '',
    }
  },
  created: function () {
    const movie_no = this.$store.state.movie_selected
    console.log(movie_no)
    axios.get(`${SERVER_URL}/movies/${movie_no}`)
      .then( (res) => {
        console.log(res.data)
        this.movie = res.data
      })
      .catch( (err) => {
        console.log(err)
      })
  }
}
</script>

<style>

</style>