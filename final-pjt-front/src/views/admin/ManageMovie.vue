<template>
  <div>
    <button @click="triggerAdd" :class="{ appear: !hideAdd || !hideUpdate }">영화추가</button>
    <AdminMovieList :class="{ appear: !hideAdd || !hideUpdate }" 
      @triggerUpdate="triggerUpdate"
    />
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