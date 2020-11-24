<template>
<div>
  
</div>
  <!-- <modal name="">
    <div>
      <h2>리뷰</h2>
    </div>
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
      <label for="content"></label>
      <textarea id="content" cols="60" rows="5" v-model="content" placeholder="감상평을 남겨주세요."></textarea>
    </div>
    <div>
      <div v-if="user_movie[login_user] && user_movie[login_user].includes(movie.id)">
        <button @click="updateReview(movie)">수정</button>
        <button @click="hide">취소</button>
      </div>
      <div v-else>
        <button @click="addReview(movie)">확인</button>
        <button @click="hide">취소</button>
      </div>
    </div>
  </modal> -->
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL

import axios from 'axios'
import { mapState } from 'vuex'


export default {
  name: 'ReviewForm',
  data: function () {
    return {
      selected_rate: null,
      like: false,
      content: null,
      // selected_rate: this.$store.state.rate,
      // like: this.$store.state.like,
      // content: this.$store.state.content,
    }
  },
  props: {
    movie: Object,
    edit: Object,
    rate_options: Array,
  },
  methods: {
    hide: function () {
      this.$modal.hide('reviewCreateForm')
      this.$store.state.content = null
      this.$store.state.rate = null
      this.$store.state.like = false

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
    addReview: function (movie) {
      const config = this.setToken()
      const reviewInfo = {
        content: this.content,
        rate: this.selected_rate,
        like: this.like,
      }

      axios.post(`${SERVER_URL}/movies/${movie.id}/review/`, reviewInfo, config)
        .then( (res) => {
          // console.log(res.data)
          const reviewerInfo = {
            movie_id: this.movie.id,
            reviewer_id: this.$store.state.login_user
          }

          this.$store.state.review_list.unshift(res.data)
          this.$store.dispatch('checkReviewer', reviewerInfo)
          this.content = null
          this.selected_rate = null
          this.like = false

          this.hide()
        })
        .catch( (err) => {
          console.log(err)
        })
    },
    updateReview: function (movie) {
      const config = this.setToken()
      const reviewInfo = {
        id: this.edit.id,
        user: this.login_user,
        movie: movie.id,
        content: this.content,
        rate: this.selected_rate,
        like: this.like,
      }
      // console.log(reviewInfo)
      axios.put(`${SERVER_URL}/movies/${movie.id}/review/update/`, reviewInfo, config)
        .then( () => {
          
          this.$emit('getAllReview')
          this.$store.state.content = null
          this.$store.state.rate = null
          this.$store.state.like = false
          this.hide()
        })
        .catch( (err) => {
          console.log(err)
        })
    },
  },
  computed: {
    ...mapState([
      'login_user',
      'user_movie',
      'review_list'
    ]),
  },
  created: function () {

  }
}
</script>

<style>

</style>