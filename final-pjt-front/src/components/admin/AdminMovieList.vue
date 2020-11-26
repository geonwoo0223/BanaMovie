<template>
  <div>

    <div class="container">
      <div class="row">
        <h1 class="font-do">영화 리스트</h1>
      </div>
      <div class="row">
        <!-- <div class="col "> -->

        <table class="table table-hover table-dark">
          <thead>
            <tr>
              <th>코드</th>
              <th>제목</th>
              <th>개봉일</th>
              <th>추천</th>
              <th>총평점</th>
              <th>수정</th>
              <th>삭제</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(movie,idx) in movies" :key="idx">
              <th>{{ movie.movie_no }}</th>
              <th>{{ movie.title }}</th>
              <th>{{ $moment(movie.release_date).format('YYYY-MM-DD') }}</th>
              <th>{{ movie.vote_count }}</th>
              <th>{{ movie.rate }}</th>
              <th><button @click="updateMovie(movie)" class="btn btn-warning font-jua">수정</button></th>
              <th><button @click="deleteMovie(movie)" class="btn btn-secondary font-jua">삭제</button></th>
            </tr>
          </tbody>


        </table>
      </div>
    </div>


  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'AdminMovieList',
  methods: {
    updateMovie: function (movie) {
      this.$router.push( { name: 'MovieUpdateForm', params: {'movie': movie}})
    },
    deleteMovie: function (movie) {
      if (confirm("이 영화를 삭제하겠습니까?"))
      axios.delete(`${SERVER_URL}/movies/${movie.id}/movie/`)
        .then( (res) => {
          const idx = this.movie_list.findIndex((movie) => {
            return movie.id === res.data.id
          })
          this.movie_list[idx].movie_no = 0

        })
        .catch( (err) => {
          console.log(err)
        })
    }
  },
  computed: {
    ...mapState([
      'movie_list',
    ]),

    movies: function () {
      return this.movie_list.filter( (movie) => {
        if (movie.movie_no) {
          return movie
        }
      })
    }
  }
}
</script>

<style>


</style>