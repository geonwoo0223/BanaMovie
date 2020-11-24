<template>
  <div>
    <div class="container" v-if="login && recommend_list.length > 0">
      <h1 class="font-do my-3">당신을 위한 영화 추천!</h1>
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
      <h1 class="font-do my-3">영화 리스트</h1>
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