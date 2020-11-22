<template>
  <div>
    <h1>Title: {{ movie.title }}</h1>
    <h3>Overview: {{ movie.overview}}</h3>
    <div v-if="login">
      <div v-if="reviewer[movie.id] && reviewer[movie.id].includes(login_user)">
        <h1>이미작성한 유저는 수정 버튼을 보여준다</h1>
        <button @click="getReview(movie)">수정</button>
      </div>
      <div v-else>
        <button @click="show">리뷰작성</button>
      </div>
      <modal name="reviewCreateForm">
        <h2>리뷰 작성</h2>
        <div>
          <label for="rate">평점</label>
          <input type="range" min="1" max="10" step="1" v-model="selected_rate">
          <select id="rate" v-model="selected_rate">
            <option v-for="(n, idx) in rate_options" :key="idx">{{n}}</option>
          </select>
        </div>
        <div>
          <label for="like">좋아요?</label>
          <input type="checkbox" id="like" checked="true" v-model="like">
          <label for="like">추천</label>
        </div>
        <div>
          <label for="review"></label>
          <textarea id="review" cols="60" rows="5" v-model.trim="review" placeholder="감상평을 남겨주세요."></textarea>
        </div>
        <div>
          <div v-if="reviewer[movie.id] && reviewer[movie.id].includes(login_user)">
            <button @click="updateReview(movie)">수정</button>
            <button >삭제</button>
            <button @click="hide">취소</button>
          </div>
          <div v-else>
            <button @click="addReview(movie)">확인</button>
            <button @click="hide">취소</button>
          </div>
        </div>
      </modal>
    </div>

    <ReviewList :movie="movie" :reviews="all_reviews"/>

  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL

import axios from 'axios'
import _ from 'lodash'
import { mapState } from 'vuex'

import ReviewList from '@/components/review/ReviewList'

export default {
  name: 'MovieDetail',
  components: {
    ReviewList,
  },
  data: function () {
    return {
      movie: '',
      selected_rate: '',
      rate_options:'',
      review: '',
      like: false,
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
    addReview: function (movie) {
      // console.log(movie)
      const config = this.setToken()
      const reviewerInfo = {
        movie_id: this.movie.id,
        reviewer_id: this.$store.state.login_user
      }
      this.$store.dispatch('checkReviewer', reviewerInfo)
      // console.log('디스패치이후',this.$store.state.reviewer)
      const reviewInfo = {
        content: this.review,
        rate: this.selected_rate,
        like: this.like,
      }

      axios.post(`${SERVER_URL}/movies/${movie.id}/review/`, reviewInfo, config)
        .then( () => {
          // console.log(res.data)
          this.review = ''
          this.selected_rate = ''
          this.hide()
          this.getAllReview()

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
          this.review = res.data['content']
          this.selected_rate = res.data['rate']
          this.like = res.data['like']
          this.show()
        })
        .catch( (err) => {
          console.log(err)
        })
    },
    updateReview: function (movie) {
      const config = this.setToken()
      const reviewInfo = {
        content: this.review,
        rate: this.selected_rate,
        like: this.like,
      }
      axios.put(`${SERVER_URL}/movies/${movie.id}/review/update/`, reviewInfo, config)
        .then( (res) => {
          console.log(res)
          this.hide()
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
      'reviewer',
    ])
  },

}
</script>

<style>

</style>