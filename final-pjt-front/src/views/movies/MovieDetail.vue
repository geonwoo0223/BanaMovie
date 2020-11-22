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
      <ReviewForm @getAllReview="getAllReview"
        :movie="movie" 
        :rate_options="rate_options"
        :review="review"
        />
    </div>

    <div>
      <h1>리뷰리스트</h1>
      <ReviewList :movie="movie" 
      v-for="(review, idx) in all_reviews"
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
      review: '',
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

    getAllReview: function () {
      axios.get(`${SERVER_URL}/movies/${this.movie.id}/reviews/`)
        .then( (res) => {
          // console.log(res.data)
          if (res.data) {
            this.all_reviews = res.data
          }
        })
        .catch( (err) => {
          console.log(err)
        })
    },

    getReview: function (movie) {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/movies/${movie.id}/review/`, config)
        .then( (res) => {
          this.review = res.data
          // this.$store.dispatch('getUpdateReviewInfo', this.review)
          this.show()
        })
        .catch( (err) => {
          console.log(err)
        })
    },
    deleteReview: function (movie) {
      this.getReview(movie)
      this.hide()
      const config = this.setToken()
      
      axios.post(`${SERVER_URL}/movies/${movie.id}/review/update/`, this.review ,config)
        .then( () => {
          for (const idx in this.$store.state.user_movie[movie.id]) {
            if (this.$store.state.user_movie[movie.id][idx] === this.login_user) {
              this.$store.state.user_movie[movie.id].splice(idx,1)
            }
          }
          this.getAllReview()
        })
        .catch( (err) => {
          console.log(err)
        })

    }
  },
  created: function () {
    this.movie = this.$route.params.movie
    this.rate_options = _.range(0,11)
    this.getAllReview()
  },
  computed: {
    ...mapState([
      'login',
      'login_user',
      'user_movie',
      'review_list',
    ])
  },
  watch: {
    // 'getReview': 'getAllReview',
    // 'deleteReview': 'getAllReview'
  }

}
</script>

<style>

</style>