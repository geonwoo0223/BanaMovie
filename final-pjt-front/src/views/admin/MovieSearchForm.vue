<template>
  <div>
    <h1>영화 추가</h1>
    <div>
      <label for="search">Search: </label>
      <input type="text" id="search" v-model.trim="search" 
        @click="searchMovie" @keypress.enter="searchMovie">
    </div>
  </div>
</template>

<script>

// import axios from 'axios'

export default {
  name: 'MovieSearchForm',
  data: function () {
    return {
      search: null,

    }
  },
  methods: {
    searchMovie: function () {
      if (this.search) {
        // axios.

        this.search = null
      }
    }
  }
  
}
</script>

<style>

</style>