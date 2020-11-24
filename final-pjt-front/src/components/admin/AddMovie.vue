<template>
  <div>
    <!-- <h2>Add Movie</h2> -->
    <div>
      <label for="title" >Title: </label>
      <input type="text" id="title" v-model.trim="title">
    </div>
    <div>
      <label for="release_date">Release Date: </label>
      <input type="date" id="release_date" v-model="release_date">
    </div>
    <div>
      <label for="adult">Adult: </label>
      <input type="checkbox" id="adult" checked="true" v-model="adult">
      <label for="adult">성인영화</label>
    </div>
    <div>
      <label for="status">Status: </label>
      <input type="checkbox" id="status" checked="true" v-model="status">
      <label for="status">상영중</label>
    </div>
    <div>
      <label for="overview">Overview: </label>
      <input type="text" id="overview" v-model.trim="overview">
    </div>
    <div>
      <label for="poster_path">Poster path: </label>
      <input type="text" id="poster_path" v-model.trim="poster_path">
    </div>
    <div class="genre">
      <div v-for="(genre,idx) in genres" :key="idx">
        <input type="checkbox" :id="genre.name" :value="genre.id" v-model="checked_genres">
        <label :for="genre.name">{{ genre.name }}</label>
      </div>
    </div>
    <br>
    <button @click="addingMovie" :class="{ appear: !hideUpdate }">추가</button>
    <button @click="updateMovie" :class="{ appear: hideUpdate }">수정</button>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL

import axios from 'axios'

export default {
  name: 'AddMovie',
  data: function () {
    return {
      genres: '',
      title: null,
      release_date: this.movie.release_date,
      adult: this.movie.adult,
      status: this.movie.status,
      overview: this.movie.overview,
      poster_path: this.movie.poster_path,
      checked_genres: this.movie.checked_genres,
      hideUpdate: !this.hideAdd
    }
  },
  props: {
    hideAdd: Boolean,
    movie: Object,
  },
  created: function () {
    this.title = this.movie.title
  
    axios.get(`${SERVER_URL}/movies/genre/`)
      .then( (res) => {
        // console.log(res.data)
        this.genres = res.data
      })
      .catch( (err) => {
        console.log(err)
      })
  },
  methods: {

    addingMovie: function () {
      const temp_number = this.$store.state.movie_count

      // poster_path가 공란이면
      if (this.poster_path === '') {
        this.poster_path = "qwodkqowfkoq.jpg"
      }

      const movieItem = {
        movieInfo: {
        movie_no: temp_number,
        title: this.title,
        release_date: this.release_date,
        poster_path: this.poster_path,
        adult: this.adult,
        overview: this.overview,
        status: this.status,
        admin_reg: true,
      }, genreInfo: {
        genres: this.checked_genres
      }}
      // console.log(movieItem)

      axios.post(`${SERVER_URL}/movies/add/`, movieItem)
        .then( (res) => {
          // console.log(res)
          this.$store.state.movie_count++
          // 영화를 만들면 자동으로 vuex에서 관리하는 영화목록에 추가
          this.$store.state.movie_list.push(res.data)
          
          this.$emit('triggerAdd')

        })
        .catch( (err) => {
          console.log(err)
          this.poster_path = ''
          alert("한번 더 확인 후 제출바랍니다.")
        })
    
    },
    updateMovie: function () {
      console.log('hi')
      console.log(this.movie)
      const temp_number = this.$store.state.movie_count

      const movieItem = {
        movie_no: temp_number,
        title: this.title,
        release_date: this.release_date,
        poster_path: this.poster_path,
        adult: this.adult,
        overview: this.overview,
        status: this.status,
        admin_reg: true,
        genres: this.checked_genres
      }

      console.log(movieItem)
      // axios.put(`${SERVER_URL}/movies/${this.movie.id}/movie/`, movieItem)
      //   .then( (res) => {
      //     console.log(res)
      //     const idx = this.movie_list.findIndex((movie) => {
      //       return movie.id === res.data.id
      //     })
      //     this.movie_list[idx] = res.data

      //   })
      //   .catch( (err) => {
      //     console.log(err)
      //     this.poster_path = ''
      //     alert("한번 더 확인 후 제출바랍니다.")
      //   })
    }
  }
}
</script>

<style scoped>
.genre {
  display: inline-block;
}

.appear {
  display: none;
}
</style>