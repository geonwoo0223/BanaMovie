<template>
  <div>
    <h1>누르면 이게 보여야돼</h1>
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
    </div>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL

import axios from 'axios'
import _ from 'lodash'
import { mapState } from 'vuex'

export default {
  name: 'ReviewCreate',
  data: function () {
    return {
      selected_rate: '',
      rate_options:'',
      review: '',
      like: false,
    }
  },
  props: {
    movie: Object,
  },
  methods: {
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
      console.log(movie)
      const config = this.setToken()

      const reviewInfo = {
        content: this.review,
        rate: this.selected_rate,
        like: this.like,
      }

      axios.post(`${SERVER_URL}/movies/${movie.id}/review/`, reviewInfo, config)
        .then( (res) => {
          console.log(res)
        })
        .catch( (err) => {
          console.log(err)
        })
    }
  },
  created: function () {
    this.rate_options = _.range(1,11)
  },
  computed: {
    ...mapState([
      'login'
    ])
  },
}
</script>

<style>

</style> 