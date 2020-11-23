<template>
  <div>
    <div v-if="login && recommend_list.length > 0">
      <h2>영화 추천 목록</h2>
      <ul>
        <li v-for="(recommend,idx) in recommend_list" :key="idx">
          {{ recommend.title }}
          <button @click="movieDetail(recommend)">임시디테일</button>
        </li>
      </ul>
    </div>
    <div>
      <h2>전체 영화 목록</h2>
    </div>
    <ul>
      <li v-for="(movie,idx) in movies" :key="idx">
        {{ movie.title }}
        <button @click="movieDetail(movie)">임시디테일</button>
      </li>
    </ul>

  </div>
</template>

<script>
import { mapState } from 'vuex'

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
    },
  },
  created: function () {
    this.movies = this.$store.state.movie_list
    if (this.login) {
      this.$store.dispatch('recommendMovie')
    }
  },
  computed: {
    ...mapState([
      'login',
      'login_user',
      'recommend_list',
    ])
  }
}
</script>

<style>

</style>