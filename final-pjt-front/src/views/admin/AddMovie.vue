<template>
  <div>

    <b-container>
      <b-row>
        <h2 class="my-3">Add Movie</h2>
        
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
      <!-- <div v-for="(genre,idx) in genres" :key="idx">
          <input type="checkbox" :id="genre.name" :value="genre.id" v-model="checked_genres">
          <label :for="genre.name">{{ genre.name }}</label>
        </div> -->
      <br>
      <b-button variant="warning" @click="addingMovie" class="my-5">Add</b-button>


    </b-container>
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
        title: '',
        release_date: '',
        adult: false,
        status: false,
        overview: '',
        poster_path: '',
        checked_genres: [],

      }
    },
    created: function () {
      axios.get(`${SERVER_URL}/movies/genre/`)
        .then((res) => {
          // console.log(res.data)
          this.genres = res.data
        })
        .catch((err) => {
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
          },
          genreInfo: {
            genres: this.checked_genres
          }
        }
        // console.log(movieItem)

        axios.post(`${SERVER_URL}/movies/add/`, movieItem)
          .then((res) => {
            console.log(res)
            this.$store.state.movie_count++
            // 영화를 만들면 자동으로 vuex에서 관리하는 영화목록에 추가
            this.$store.state.movie_list.push(res.data)

            // 영화 만들면 detail 페이지로 
            this.$router.push({
              name: 'MovieDetail',
              params: {
                'movie': res.data
              }
            })
          })
          .catch((err) => {
            console.log(err)
            this.poster_path = ''
            alert("한번 더 확인 후 제출바랍니다.")
          })


      }
    }
  }
</script>

<style scoped>
  .genre {
    display: inline;
  }
</style>