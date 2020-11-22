import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movie_list: [],
    login: false,
    login_user: '',
    is_admin: '',
    movie_count: 50000000,
    username: '', 
    reviewer: {},
    // update_review_info: {
    //   selected_rate: '',
    //   content: '',
    //   like: false,
    // },
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
      if (state.reviewer[`${movie_id}`]) {
        state.reviewer[`${movie_id}`].push(reviewer_id)
      } else {
        state.reviewer[`${movie_id}`] = [reviewer_id]
      }
    },
    // GET_UPDATE_REVIEW_INFO: function (state, review_info) {
    //   state.update_review_info = review_info
    // }
  },
  actions: {
    getMovie: function ({commit}, movies) {
      commit('GET_MOVIE', movies)
    },
    checkReviewer: function ({commit}, reviewerInfo) {
      commit('CHECK_REVIEWER', reviewerInfo)
    },
    // getUpdateReviewInfo: function ({commit}, review_info) {
    //   commit('GET_UPDATE_REVIEW_INFO', review_info)
    // }

  },
})
