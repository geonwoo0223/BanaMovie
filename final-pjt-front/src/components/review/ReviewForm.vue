<template>
  <modal name="reviewCreateForm">
    <div v-if="reviewer[movie.id] && reviewer[movie.id].includes(login_user)">
      <h2>리뷰 수정</h2>
    </div>
    <div v-else>
      <h2>리뷰 작성</h2>
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
      <textarea id="content" cols="60" rows="5" v-model.trim="content" placeholder="감상평을 남겨주세요."></textarea>
    </div>
    <div>
      <div v-if="reviewer[movie.id] && reviewer[movie.id].includes(login_user)">
        <button @click="updateReview(movie)">수정</button>
        <button @click="temp">삭제</button>
        <button @click="hide">취소</button>
      </div>
      <div v-else>
        <button @click="addReview(movie)">확인</button>
        <button @click="hide">취소</button>
      </div>
    </div>
  </modal>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL

import axios from 'axios'
import { mapState } from 'vuex'


export default {
  name: 'ReviewForm',
  data: function () {
    return {
      // selected_rate: this.review['selected_rate'],
      // like: this.review['like'],
      // content: this.review['content'],
      selected_rate: '',
      like: false,
      content: '',
    }
  },
  props: {
    movie: Object,
    review: Object,
    rate_options: Array,
  },
  methods: {
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
        content: this.content,
        rate: this.selected_rate,
        like: this.like,
      }

      axios.post(`${SERVER_URL}/movies/${movie.id}/review/`, reviewInfo, config)
        .then( () => {
          // console.log(res.data)
          this.content = ''
          this.selected_rate = ''
          this.like = false
          this.hide()
          this.$emit('getAllReview')
        })
        .catch( (err) => {
          console.log(err)
        })
    },
    updateReview: function (movie) {
      const config = this.setToken()
      const reviewInfo = {
        content: this.content,
        rate: this.selected_rate,
        like: this.like,
      }
      axios.put(`${SERVER_URL}/movies/${movie.id}/review/update/`, reviewInfo, config)
        .then( (res) => {
          console.log(res)
          this.hide()
          this.$emit('getAllReview')

        })
        .catch( (err) => {
          console.log(err)
        })
    },
    temp: function () {
      console.log(this.review)
    }
  },
  created: function () {
    console.log(this.review)
    this.selected_rate= this.review['selected_rate']
    this.like= this.review['like']
    this.content= this.review['content']
  },
  computed: {
    ...mapState([
      'login_user',
      'reviewer',
    ])
  },
}
</script>

<style>

</style>