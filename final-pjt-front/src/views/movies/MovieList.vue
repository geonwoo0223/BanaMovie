<template>
  <div>
    <ul>
      <li v-for="(movie,idx) in movies" :key="idx">{{ movie.title }}</li>
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
  created: function () {

    this.movies = this.$store.state.movie_list

    console.log(this.movies)

  }
}
</script>

<style>

</style>