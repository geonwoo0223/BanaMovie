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



export default {
  name: 'ManageMovie',
  components: {
    AdminMovieList,
  },
  data: function () {
    return {
      hideAdd: true,
      hideUpdate: true,
    }
  },
  methods: {
    triggerAdd: function () {
      this.$router.push({name : 'MovieAddForm'})
    },
    triggerUpdate: function (movie) {
      this.hideUpdate = false
      this.$store.state.temp = movie
      console.log(this.$store.state.temp)
    }
  },
}
</script>

<style scoped>

.appear {
  display: none;
}

</style>