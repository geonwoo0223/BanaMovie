<template>
  <div class="col-3 my-3">
    <button>
      <img 
      @click="showDetail"
      :src="movie.poster_path" 
      :alt="movie.title"
      />
    </button>




    <!-- 영화눌렀을때 이게 보이게 한다 -->
    <b-modal
      hide-footer 
      v-model="show"
      :title="movie.title">
      <!-- 영화디테일 부분 -->
      <img :src="movie.poster_path" alt="movie poster">
      <h5>개봉: {{ movie.release_date }}</h5>
      <h5 v-if="movie.overview">줄거리: {{ movie.overview }}</h5>
      <!-- 리뷰부분 -->
      <div v-if="is_admin === false" :class="{ appear: showForm }">
        <div id="reviewForm">
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
            <div>
              <button :class="{ appear: showAdd }" @click="addReview(movie)">확인</button>
              <button :class="{ appear: !showAdd }" @click="updateReview(movie)">수정</button>
              <button @click="hideDetail">취소</button>
            </div>
          </div>
        </div>
      </div>

      <!-- 리뷰목록 -->
      <h3>리뷰목록</h3>
      <div v-for="(review,idx) in review_list" :key="idx">
        <div v-if="review.movie.id === movie.id || review.id === movie.id">
          유저 {{ review.user.username }}이/가 작성한 리뷰 "{{ review.content }}" 평점: {{review.rate}}
          <div v-if="review.user.id === login_user">
            <button @click="updateReady(review)">수정</button>
            <button @click="deleteReview(movie)">삭제</button>
          </div>
        </div>
      </div>

    </b-modal>

  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL

import axios from 'axios'
import _ from 'lodash'
import { mapState } from 'vuex'

export default {
  name: 'MovieListItem',
  props: {
    movie: Object
  },
  data: function () {
    return {
      selected_rate: null,
      like: false,
      content: null,
      show: false,
      showForm: false,
      showAdd: false,
      reviewId: null,
      rate_options: _.range(0,11),
    }
  },
  methods: {
    showDetail: function () {
      this.show = true
    },
    hideDetail: function () {
      this.show = false
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
            reviewer_id: res.data.user.id
          }

          this.$store.state.review_list.unshift(res.data)
          this.$store.dispatch('checkReviewer', reviewerInfo)
          this.content = null
          this.selected_rate = null
          this.like = false
          this.showForm = true
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
          this.showForm = false
          this.showAdd = false
        })
        .catch( (err) => {
          console.log(err)
        })

    },
    updateReady: function (review) {
      this.content = review.content
      this.like = review.like
      this.selected_rate = review.rate
      this.showForm = false
      this.showAdd = true
      this.reviewId = review.id
    },

    updateReview: function (movie) {
      const config = this.setToken()
      const reviewInfo = {
        id: this.reviewId,
        user: this.login_user,
        movie: movie.id,
        content: this.content,
        rate: this.selected_rate,
        like: this.like,
      }
      axios.put(`${SERVER_URL}/movies/${movie.id}/review/update/`, reviewInfo, config)
        .then( (res) => {
          this.content = null
          this.like = false
          this.selected_rate = null
          this.showForm = true
          this.showAdd = false
          this.reviewId = null
          console.log(res)
          const idx = this.review_list.findIndex((review) => {
            return review.id === res.data.id
          })
          this.$store.state.review_list[idx].content = res.data.content
        })
        .catch( (err) => {
          console.log(err)
        })
    },

  },
  created: function () {
    if (this.user_movie[this.login_user] && this.user_movie[this.login_user].includes(this.movie.id)) {
      this.showForm = true
    }
  },
  computed: {
    ...mapState([
      'login_user',
      'is_admin',
      'user_movie',
      'review_list',
    ])
  }
}
</script>

<style scoped>

.appear {
  display: none;
}

</style>