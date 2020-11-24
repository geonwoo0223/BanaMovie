<template>
  <div>
    <b-container>
      <b-row>

  <b-button size="lg" block pill variant="light" @click="triggerAdd" :class="{ appear: !hideAdd }" class="my-5 font-do" >영화 추가</b-button>
    <AddMovie :class="{ appear: hideAdd }" 
      @triggerAdd="triggerAdd" :hideAdd="hideAdd" :movie="movie" 
    />
      </b-row>

      <!-- <b-row> -->
        
    <AdminMovieList :class="{ appear: !hideAdd }" 
      @triggerUpdate="triggerUpdate"
    />
      <!-- </b-row>-->

    </b-container>



   


  </div>
</template>

<script>

import AdminMovieList from '@/components/admin/AdminMovieList'
import AddMovie from '@/components/admin/AddMovie'



export default {
  name: 'ManageMovie',
  components: {
    AdminMovieList,
    AddMovie,
  },
  data: function () {
    return {
      hideAdd: true,
      movie: {
        title: null,
        release_date: null,
        adult: false,
        status: false,
        overview: null,
        poster_path: null,
        checked_genres: [],
      },
    }
  },
  methods: {
    triggerAdd: function () {
      this.hideAdd = !this.hideAdd
    },
    triggerUpdate: function (movie) {
      this.hideAdd = !this.hideAdd
      // console.log(movie)
      this.movie.title = movie.title
      this.movie.release_date = movie.release_date
      this.movie.adult = movie.adult
      this.movie.status = movie.status
      this.movie.overview = movie.overview
      this.movie.poster_path = movie.poster_path
      for (const genre of movie.genres) {
        this.movie.checked_genres.push(genre.id)
      }
      console.log(this.movie)
    }
  }


  
}
</script>

<style scoped>

.appear {
  display: none;
}

</style>