<template>
  <div>
    <b-container class="mb-5">
      <b-row class="d flex justify-content-center">
        <h1 class="font-do my-3">화제작</h1>
      </b-row>
      <b-row>

      
      
        <!-- 영화 슬라이드 넣을 공간  -->
        <b-col>
          <b-carousel id="carousel-1" v-model="slide" :interval="2000" controls indicators background="#ababab"
              style="text-shadow: 1px 1px 2px #333;" @sliding-start="onSlideStart"
            @sliding-end="onSlideEnd"
            class="font-poor">

            <b-carousel-slide v-for="(movie, idx) in ordered_movie_list" :key="idx" :caption="movie.title" 
              img-blank-color="dark" img-height="480" style="background: #343a40;">
              <template #img>
                <img class="d-block img-fluid " :src="movie.poster_path" alt="image slot">
              </template>
              <p>{{ movie.overview | truncate(300, '...') }}</p>
            </b-carousel-slide>
          </b-carousel>

          <!-- <p class="mt-4">
            Slide #: {{ slide }}<br>
            Sliding: {{ sliding }}
          </p> -->
        </b-col>
      </b-row>

    </b-container>



    <div class="container" v-if="login && recommend_list.length > 0">
      <h1 class="font-do my-3">당신을 위한 영화 추천!</h1>
      <div class="row">
        <MovieListItem v-for="(movie,idx) in recommend_list" :key="idx" :movie="movie" class="col-3" />
      </div>
    </div>

    
    <div>
      <h1 class="font-do my-5">영화 리스트</h1>
    </div>
    <div class="container">
      <!-- <div class="row justify-content-end mb-4">
        <label class="h2 mr-3" for="">Search: </label>
        <input style="width: 300px;" class="form-control" type="text" v-model.trim='search'>
      </div> -->
      <div class="row">
        <MovieListItem v-for="(movie,idx) in movies" :key="idx" :movie="movie" class="col-3" :search="search"/>
      </div>
    </div>

  </div>
</template>

<script>
  import {
    mapState
  } from 'vuex'

  import MovieListItem from '@/components/movie/MovieListItem'

  export default {
    name: 'MovieList',
    data: function () {
      return {
        slide: 0,
        sliding: null,
        search: '',
      }
    },
    components: {
      MovieListItem,
    },
    methods: {
      movieDetail: function (movie) {
        this.$router.push({
          name: 'MovieDetail',
          params: {
            'movie': movie
          }
        })
      },
      onSlideStart() {
        this.sliding = true
      },
      onSlideEnd() {
        this.sliding = false
      },
    },
    created: function () {

      if (this.login && this.is_admin === false) {
        this.$store.dispatch('recommendMovie')
      }
    },
    computed: {
      ...mapState([
        'login',
        'login_user',
        'is_admin',
        'movie_list',
        'ordered_movie_list',
        'recommend_list',
      ]),

      movies: function () {
        return this.movie_list.filter( (movie) => {
          if (movie.movie_no) {
            return movie
          }
        })
      }
    }
  }
</script>

<style>

.carousel-caption {
  position: absolute;
  right: 15%;
  bottom: 20px;
  left: 25% !important;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  /* text-align: center; */
}


</style>