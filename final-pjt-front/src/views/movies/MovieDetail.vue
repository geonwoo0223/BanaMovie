<template>
  <div>
    <h1>Title: {{ movie.title }}</h1>
    <h3>Overview: {{ movie.overview}}</h3>
    <!-- <div v-if="login"> -->
    <div>
      <h1>로그인한 유저만 보여</h1>
      <ReviewCreate :movie="movie"/>
    </div>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL

import axios from 'axios'
import { mapState } from 'vuex'
import ReviewCreate from '@/components/ReviewCreate'


export default {
  name: 'MovieDetail',
  components: {
    ReviewCreate,
  },
  data: function () {
    return {
      movie: '',
    }
  },
  methods: {
    
  },
  created: function () {
    const movie_no = this.$store.state.movie_selected
    // console.log(movie_no)
    axios.get(`${SERVER_URL}/movies/${movie_no}`)
      .then( (res) => {
        console.log(res.data)
        this.movie = res.data
      })
      .catch( (err) => {
        console.log(err)
      })
  },
  computed: {
    ...mapState([
      'login'
    ])
  }
}
</script>

<style>

</style>