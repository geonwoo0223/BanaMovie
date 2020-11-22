import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // 영화 관련
    movie_list: [],
    review_list: [],
    movie_count: 50000000,
    user_movie: {},

    // 로그인 관련
    login: false,
    login_user: '',
    is_admin: false,
    
    // 커뮤니티 관련
    comments: [],
    

  },
  getters: {

  },
  mutations: {
    GET_MOVIE: function (state, movies) {
      for (const movie of movies) {
        state.movie_list.push(movie)
      }
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
  },
  },
  actions: {
    getMovie: function ({commit}, movies) {
      commit('GET_MOVIE', movies)
    },
    checkReviewer: function ({commit}, reviewerInfo) {
      commit('CHECK_REVIEWER', reviewerInfo)
    },
  },

})
