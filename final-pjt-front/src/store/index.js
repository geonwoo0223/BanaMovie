import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // 영화 관련
    movie_list: [],
    ordered_movie_list: [],
    review_list: [],
    recommend_list: [],
    movie_count: 50000000,
    user_movie: {},
    temp: {
      title: '',
      release_date: '',
      adult: false,
      status: false,
      overview: '',
      poster_path: '',
      genres: [],
    },

    // 리뷰 관련
    content: null,
    like: false,
    rate: null,
    review_update:'', 

    // 로그인 관련
    login: false,
    login_user: null,
    is_admin: false,
    username: null,
    
    // 커뮤니티 관련
    comments: [],
    

  },
  getters: {
    
  },
  mutations: {
    IS_ADMIN: function (state, status) {
      // console.log(status)
      state.is_admin = status
    },
    GET_MOVIE: function (state) {
      axios.get(`${SERVER_URL}/movies/`)
        .then( (res) => {
          const movies = res.data
            for (const movie of movies) {
              state.movie_list.push(movie)
              state.ordered_movie_list.push(movie)
            }
          state.ordered_movie_list.sort( (a,b) => {
            return parseFloat(b.vote_count) - parseFloat(a.vote_count)})
        })
        .catch( (err) => {
          console.log(err)
        })
    },
    CHECK_REVIEWER: function (state, reviewerInfo) {
      const movie_id = reviewerInfo['movie_id']
      const reviewer_id = reviewerInfo['reviewer_id']
      if (state.user_movie[`${reviewer_id}`]) {
        state.user_movie[`${reviewer_id}`].push(movie_id)
      } else {
        state.user_movie[`${reviewer_id}`] = [movie_id]
      }
      console.log("{유저:[영화]", state.user_movie)
      console.log(state.review_list)
    },
    RECOMMEND_MOVIE: function (state, id) {
      // console.log(state.is_admin)
      if (state.is_admin) {
        state.recommend_list = []
      } else {
        if (!id) {
          id = state.login_user
        }
        if (state.login_user) {
          axios.get(`${SERVER_URL}/movies/recommend/${id}/`)
            .then( (res) => {
              // console.log(res)
              state.recommend_list = res.data
              // console.log(state.recommend_list)
            })
            .catch( (err) => {
              console.log(err)
            })
        }
      }        
    }
  },
  actions: {
    isAdmin: function ({commit}, status) {
      commit('IS_ADMIN', status)
    },
    getMovie: function ({commit}) {
      commit('GET_MOVIE')
    },
    checkReviewer: function ({commit}, reviewerInfo) {
      commit('CHECK_REVIEWER', reviewerInfo)
    },
    recommendMovie: function ({commit}, id) {
      commit('RECOMMEND_MOVIE', id)
    }
  },

})
