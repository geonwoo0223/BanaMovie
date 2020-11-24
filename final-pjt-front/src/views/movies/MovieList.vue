<template>
  <div>
    <div class="container" v-if="login && recommend_list.length > 0">
      <h2>영화 추천 목록</h2>
      <div class="row">
        <MovieListItem 
          v-for="(movie,idx) in recommend_list"
          :key="idx"
          :movie="movie"
          class="col-3"
        /> 
    </div>
    </div>
    <div>
      <h2>전체 영화 목록</h2>
    </div>
    <div class="container">
      <div class="row">
        <MovieListItem 
          v-for="(movie,idx) in movie_list"
          :key="idx"
          :movie="movie"
          class="col-3"
        /> 
      </div>
    </div>

  </div>
</template>

<script>

import { mapState } from 'vuex'

import MovieListItem from '@/components/movie/MovieListItem'

export default {
  name: 'MovieList',
  data: function () {
    return {
    }
  },
  components: {
    MovieListItem,
  },
  methods: {
    movieDetail: function (movie) {
      this.$router.push({ name: 'MovieDetail', params: {'movie': movie} })
    },
  },
  created: function () {
    this.$store.dispatch('getMovie')
    if (this.login && this.is_admin === false) {
      this.$store.dispatch('recommendMovie')
    }
  },
  computed: {
    ...mapState([
      'login',
      'login_user',
      'is_admin',
      'movie_list',
      'recommend_list',
    ]),
  }
}
</script>

<style>

</style>