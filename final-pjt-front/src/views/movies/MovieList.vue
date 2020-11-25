<template>
  <div>
    <b-container>
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
            <!-- Text slides with image -->
            <b-carousel-slide caption="First slide" text="Nulla vitae elit libero, a pharetra augue mollis interdum."
              img-src="https://picsum.photos/1024/480/?image=52">
            </b-carousel-slide>

            <!-- Slides with custom text -->
            <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=54">
              <h1>Hello world!</h1>
            </b-carousel-slide>

            <!-- Slides with image only -->
            <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=58"></b-carousel-slide>

            <!-- Slides with img slot -->
            <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
            <b-carousel-slide v-for="(movie,idx) in movie_list" :key="idx" :caption="movie.title"
              :text="movie.overview" img-blank-color="dark" img-height="480">
              <template #img>
                <img class="d-block img-fluid " :src="movie.poster_path" alt="image slot">
              </template>
            </b-carousel-slide>

            <!-- Slide with blank fluid image to maintain slide aspect ratio -->
            <b-carousel-slide caption="Blank Image" img-blank img-blank-color="dark" img-alt="Blank image">
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eros felis, tincidunt
                a tincidunt eget, convallis vel est. Ut pellentesque ut lacus vel interdum.
              </p>
            </b-carousel-slide>
          </b-carousel>

          <p class="mt-4">
            Slide #: {{ slide }}<br>
            Sliding: {{ sliding }}
          </p>
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
      <h1 class="font-do my-3">영화 리스트</h1>
    </div>
    <div class="container">
      <div class="row">
        <MovieListItem v-for="(movie,idx) in movie_list" :key="idx" :movie="movie" class="col-3" />
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
        sliding: null
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
      }
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
        'recommend_list',
      ]),
    }
  }
</script>

<style>

</style>