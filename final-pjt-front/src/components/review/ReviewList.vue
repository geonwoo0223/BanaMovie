<template>
  <div>
   <div v-if="review.movie.id === movie.id || review.id === movie.id">
    유저 {{ review.user.username }}이/가 작성한 리뷰 "{{ review.content }}" 평점: {{review.rate}}
   </div>
  </div>
</template>

<script>

// import { mapState } from 'vuex'


export default {
  name: 'ReviewList',
  data: function () {
    return {
    }
  },
  props: {
    movie: Object,
    review: Object,
  },

}

</script>

<style>

</style>