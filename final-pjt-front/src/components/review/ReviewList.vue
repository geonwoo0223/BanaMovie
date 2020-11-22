<template>
  <div>
   <div>
    유저 {{ review.user.username }}이/가 작성한 리뷰 "{{ review.content }}" 평점: {{review.rate}}
   </div>
  </div>
</template>

<script>

import { mapState } from 'vuex'


export default {
  name: 'ReviewList',
  data: function () {
    return {
      reviews: '',
    }
  },
  props: {
    movie: Object,
    review: Object,
  },
  mounted: function () {
    this.reviews = this.review_list[this.movie.id]
  },
  computed: {
    ...mapState([
      'login_user',
      'review_list'
    ])
  },
}

</script>

<style>

</style>