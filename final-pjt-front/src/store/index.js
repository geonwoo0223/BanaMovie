import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movie_list: [],
    // is_admin: false,
  },
  getters: {

  },
  mutations: {
    GET_MOVIE: function (state, movies) {
      for (const movie of movies) {
        state.movie_list.push(movie)
      }
    }
  },
  actions: {
    getMovie: function ({commit}, movies) {
      commit('GET_MOVIE', movies)
    }
  },
})
