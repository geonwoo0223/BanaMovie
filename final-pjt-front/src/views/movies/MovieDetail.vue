<template>
  <div>
    <h1>Title: {{ movie.title }}</h1>
    <h3>Overview: {{ movie.overview}}</h3>
    <div v-if="login">
      <div v-if="user_movie[login_user] && user_movie[login_user].includes(movie.id)">
        <h1>이미작성한 유저는 수정 버튼을 보여준다</h1>
        <button @click="getReview(movie)">수정</button>
        <button @click="deleteReview(movie)">삭제</button>
      </div>
      <div v-else>
        <button @click="show">리뷰작성</button>
      </div>
      <ReviewForm @getAllReview="getAllReview(movie)"
        :movie="movie" 
        :rate_options="rate_options"
        :edit="edit"
        />
    </div>

    <div>
      <h1>리뷰리스트</h1>
      <ReviewList :movie="movie" 
      v-for="(review, idx) in review_list"
      :key="idx" :review="review"
      />
    </div>

  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL

import axios from 'axios'
import _ from 'lodash'
import { mapState } from 'vuex'

import ReviewList from '@/components/review/ReviewList'
import ReviewForm from '@/components/review/ReviewForm'

export default {
  name: 'MovieDetail',
  components: {
    ReviewList,
    ReviewForm,
  },
  data: function () {
    return {
      edit: {},
      movie: '',
      rate_options:'',
      all_reviews: '',
    }
  },
  methods: {
    show: function () {
      this.$modal.show('reviewCreateForm')
    },
    hide: function () {
      this.$modal.hide('reviewCreateForm')
    },

    setToken: function () {
      const token = localStorage.getItem('jwt')

      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    
    getAllReview: function (movie) {
      axios.get(`${SERVER_URL}/movies/${movie.id}/reviews/`)
        .then( (res) => {
          // console.log(res.data)
          this.$store.state.review_list = res.data
        })
        .catch( (err) => {
          console.log(err)
        })
    },

    getReview: function (movie) {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/movies/${movie.id}/review/`, config)
        .then( (res) => {
          // console.log(res.data)
          this.edit = res.data
          console.log(res.data)
          this.show()
        })
        .catch( (err) => {
          console.log(err)
        })
    },

    deleteReview: function (movie) {
      const config = this.setToken()
      
      axios.delete(`${SERVER_URL}/movies/${movie.id}/review/update/`, config)
        .then( (res) => {
          console.log(res)
          const idx1 = this.review_list.indexOf(res.data.id)
          this.$store.state.review_list.splice(idx1,1)

          const idx2 = this.user_movie[this.login_user].indexOf(movie.id)
          this.$store.state.user_movie[this.login_user].splice(idx2,1)

        })
        .catch( (err) => {
          console.log(err)
        })

    }
  },
  created: function () {
    this.movie = this.$route.params.movie
    this.rate_options = _.range(0,11)
    this.getAllReview(this.movie)
  },
  computed: {
    ...mapState([
      'login',
      'login_user',
      'user_movie',
      'review_list',
    ])
  },

}
</script>

<style>

</style>