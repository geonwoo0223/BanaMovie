<template>
  <div>
    <b-container>
      <b-row>
        <b-col sm='6'>
          <b-button size="lg" block pill variant="light" @click="triggerAdd" :class="{ appear: !hideAdd }" class="my-5 font-do" >직접 추가</b-button>
        </b-col>
        <b-col sm='6'>
          <b-button size="lg" block pill variant="light" @click="triggerSearch" :class="{ appear: !hideAdd }" class="my-5 font-do" >검색 추가</b-button>
        </b-col>
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
    triggerSearch: function () {
      this.$router.push({name : 'MovieSearchForm'})
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