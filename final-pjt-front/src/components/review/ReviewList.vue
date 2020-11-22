<template>
  <div>
    <h1>리뷰리스트</h1>
    <h3> {{ movie.title }} </h3>
    <ul>
      <li v-for="(review,idx) in reviews" :key="idx"> 
        {{ review.content }}
        <!-- <button v-if="">수정</button> -->

      </li>
    </ul>
  </div>
</template>

<script>

import { mapState } from 'vuex'


export default {
  name: 'ReviewList',
  data: function () {
    return {
    }
  },
  props: {
    movie: Object,
    reviews: [Array, String],
  },
  created: function () {
  },
  computed: {
    ...mapState([
      'login',
      'login_user',
    ])
  }
}

</script>

<style>

</style>