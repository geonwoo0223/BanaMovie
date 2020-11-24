<template>
  <div>
   
    <div class="container">
      <div class="row">
        <h1 class="font-do">영화 리스트</h1>
      </div>
      <div class="row">
        <!-- <div class="col "> -->

          <table class="table table-hover table-dark" >
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
              <tr v-for="(movie,idx) in movie_list" :key="idx">
                <th>{{ movie.movie_no }}</th>
                <th>{{ movie.title }}</th>
                <th>{{ $moment(movie.release_date).format('YYYY-MM-DD') }}</th>
                <th>{{ movie.vote_count }}</th>
                <th>{{ movie.rate }}</th>
                <th><button @click="updateMovie(movie)">수정</button></th>
                <th><button @click="deleteMovie(movie)">삭제</button></th>
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

  import {
    mapState
  } from 'vuex'

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
    computed: {
      ...mapState([
        'movie_list',
      ])
    }
  },
</script>

<style>


</style>