<template>
  <div>
    <b-container>
      <b-row class="d-flex justify-content-center">
        <h1 class="my-5 font-do">영화 추가</h1>
        
      </b-row>



      <b-row class="my-1">
        <b-col sm="2" offset="2">
          <label for="title">Title: </label>
        </b-col>
        <b-col sm="6">
          <b-form-input id="title" v-model.trim="title"></b-form-input>
        </b-col>
      </b-row>

      <b-row class="my-3">
        <b-col sm="2" offset="2">
          <label for="release_date">Release Date: </label>
        </b-col>
        <b-col sm="6">
          <input type="date" id="release_date" v-model="release_date">
        </b-col>
      </b-row>


      <b-row class="my-3">
        <b-col sm="2" offset="2">
          <label for="adult">Adult: </label>
        </b-col>
        <b-col sm="6">
          <input type="checkbox" id="adult" checked="true" v-model="adult">
          <label for="adult">성인영화</label>
        </b-col>
      </b-row>


      <b-row class="my-3">
        <b-col sm="2" offset="2">
          <label for="status">Status: </label>
        </b-col>
        <b-col sm="6">
          <input type="checkbox" id="status" checked="true" v-model="status">
          <label for="status">상영중</label>
        </b-col>
      </b-row>


      <b-row class="my-3">
        <b-col sm="2" offset="2">
          <label for="overview">Overview: </label>
        </b-col>
        <b-col sm="6">
          <input type="text" id="overview" v-model.trim="overview">
        </b-col>
      </b-row>

      <b-row class="my-3">
        <b-col sm="2" offset="2">
          <label for="poster_path">Poster path: </label>
        </b-col>
        <b-col sm="6">
          <input type="text" id="poster_path" v-model.trim="poster_path">
        </b-col>
      </b-row>
      <b-row class="my-3">
        <b-col sm="2" offset="2">
          <label>Genres: </label>
        </b-col>
      </b-row>

      <b-row class="my-3">
        <b-col sm="4" offset="5">
            <b-form-checkbox-group v-for="(genre,idx) in genres" :key="idx" inline >
              <b-form-checkbox :id="genre.name" :value="genre.id" v-model="checked_genres" inline >{{ genre.name }}
              </b-form-checkbox>
            </b-form-checkbox-group>
        </b-col>
      </b-row>

      <br>
      <b-button variant="warning" @click="addMovie" class="my-5">추가</b-button>

    </b-container>

  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL
import axios from 'axios'


export default {
  name: 'MovieAddForm',
  data: function () {
    return {
      genres: '',
      title: null,
      release_date: null,
      adult: false,
      status: false,
      overview: null,
      poster_path: null,
      checked_genres: [],
    }
  },
  created: function () {
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

    addMovie: function () {
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
        .catch((err) => {
          console.log(err)
        })
    },
  }
}
</script>

<style>

</style>