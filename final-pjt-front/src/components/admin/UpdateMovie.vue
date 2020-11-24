<template>
  <div>

    <b-container>
      <b-row>
        <h2 class="my-3">영화 수정</h2>
        
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
      <b-button variant="warning" @click="updateMovie" class="my-5">수정</b-button>
    </b-container>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL

import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'UpdateMovie',
  data: function () {
    return {
      genres: '',
      title: this.temp.title,
      release_date: '',
      adult: false,
      status: false,
      overview: '',
      poster_path: '',
      checked_genres: [],
    }
  },
  created: function () {
    console.log("이거 언제 찍히지", this.temp)
  
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

    updateMovie: function () {

      const movieItem = {
        movie_no: '',
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
    //   axios.put(`${SERVER_URL}/movies/${this.movie.id}/movie/`, movieItem)
    //     .then( (res) => {
    //       console.log(res)
    //       const idx = this.movie_list.findIndex((movie) => {
    //         return movie.id === res.data.id
    //       })
    //       this.movie_list[idx] = res.data

    //     })
    //     .catch( (err) => {
    //       console.log(err)
    //       this.poster_path = ''
    //       alert("한번 더 확인 후 제출바랍니다.")
    //     })
    }
  },
  computed :{
    ...mapState([
      'temp',
    ])
  },
  watch: {
    triggerUpdate: function () {
      console.log("봤어?")
    }
  }
}
</script>

<style>

</style>