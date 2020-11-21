<template>
  <div>
    <h1>Title: {{ movie.title }}</h1>
    <h3>Overview: {{ movie.overview}}</h3>
    <p>{{movie.id}}</p>
    <div v-if="login">
      <div v-if="reviewer[movie.id] && reviewer[movie.id].includes(login_user)">
        <h1>이미작성한 유저</h1>
      </div>
      <div v-else>
        <button @click="show">리뷰작성</button>
        <modal name="reviewCreateForm">
          <h2>리뷰 작성</h2>
          <div>
            <label for="rate">평점</label>
            <input type="range" min="1" max="10" step="1" value="5" v-model="selected_rate">
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
            <button @click="addReview(movie)">확인</button>
            <button @click="hide">취소</button>
          </div>
        </modal>
      </div>
    </div>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL

import axios from 'axios'
import _ from 'lodash'
import { mapState } from 'vuex'


export default {
  name: 'MovieDetail',
  data: function () {
    return {
      movie: '',
      selected_rate: '',
      rate_options:'',
      review: '',
      like: false,
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

    addReview: function (movie) {
      // console.log(movie)
      const config = this.setToken()
      const reviewerInfo = {
        movie_id: this.movie.id,
        reviewer_id: this.$store.state.login_user
      }
      this.$store.dispatch('checkReviewer', reviewerInfo)
      console.log('디스패치이후',this.$store.state.reviewer)
      const reviewInfo = {
        content: this.review,
        rate: this.selected_rate,
        like: this.like,
      }

      axios.post(`${SERVER_URL}/movies/${movie.id}/review/`, reviewInfo, config)
        .then( () => {
          // console.log(res.data.user[0])
          this.$modal.hide('reviewCreateForm')
          this.review = ''
          this.selected_rate = ''
        })
        .catch( (err) => {
          console.log(err)
        })
    }
  },
  created: function () {
    const movie_id = this.$route.params.id
    axios.get(`${SERVER_URL}/movies/${movie_id}`)
      .then( (res) => {
        // console.log(res.data)
        this.movie = res.data
      })
      .catch( (err) => {
        console.log(err)
      })
    
    this.rate_options = _.range(0,11)
    console.log('들어오면',this.$store.state.reviewer)

  },
  computed: {
    ...mapState([
      'login',
      'login_user',
      'reviewer',
    ])
  }
}
</script>

<style>

</style>