<template>
  <div>
    <ul>
      <li v-for="(movie,idx) in movies" :key="idx">
        {{ movie.title }}
        <button @click="movieDetail(movie)">임시디테일</button>
      </li>
    </ul>

  </div>
</template>

<script>

// import { mapState } from 'vuex'

export default {
  name: 'MovieList',
  data: function () {
    return {
      movies: '',
    }
  },
  methods: {
    movieDetail: function (movie) {
      this.$router.push({ name: 'MovieDetail', params: {'movie': movie} })
    }
  },
  created: function () {

    this.movies = this.$store.state.movie_list

    // console.log(this.movies)

  }
}
</script>

<style>

</style>