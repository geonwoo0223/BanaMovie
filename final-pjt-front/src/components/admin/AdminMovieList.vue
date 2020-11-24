<template>
  <div>
    <table border=1>
      <tr>
        <th>코드</th>
        <th>제목</th>
        <th>개봉일</th>
        <th>추천</th>
        <th>총평점</th>
        <th>수정</th>
        <th>삭제</th>
      </tr>
      <tr v-for="(movie,idx) in movie_list" :key="idx">
        <th>{{ movie.movie_no }}</th>
        <th>{{ movie.title }}</th>
        <th>{{ $moment(movie.release_date).format('YYY-MM-DD') }}</th>
        <th>{{ movie.vote_count }}</th>
        <th>{{ movie.rate }}</th>
        <th><button @click="updateMovie(movie)">수정</button></th>
        <th><button @click="deleteMovie(movie)">삭제</button></th>
   
      </tr>


    </table>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL

import axios from 'axios'

import { mapState } from 'vuex' 

export default {
  name: 'AdminMovieList',
  data: function () {
    return {
      show: false
    }
  },
  methods: {
    updateMovie: function (movie) {
      // console.log(movie.id)
      this.$emit('triggerUpdate', movie)
    },
    deleteMovie: function (movie) {
      axios.delete(`${SERVER_URL}/movies/${movie.id}/movie/`)
        .then( (res) => {
          const idx = this.movie_list.findIndex((movie) => {
            return movie.id === res.data.id
          })
          this.movie_list.splice(idx,1)

        })
        .catch( (err) => {
          console.log(err)
        })
    }
  },
  computed: {
    ...mapState([
      'movie_list',
    ])
  },
}
</script>

<style>

</style>