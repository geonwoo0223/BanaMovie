<template>
  <div>
    <button @click="triggerAdd" :class="{ appear: !hideAdd }">영화추가</button>
    <AddMovie :class="{ appear: hideAdd }" 
      @triggerAdd="triggerAdd" :hideAdd="hideAdd" :movie="movie" 
    />
    <AdminMovieList :class="{ appear: !hideAdd }" 
      @triggerUpdate="triggerUpdate"
    />
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
        title: '',
        release_date: '',
        adult: false,
        status: false,
        overview: '',
        poster_path: '',
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