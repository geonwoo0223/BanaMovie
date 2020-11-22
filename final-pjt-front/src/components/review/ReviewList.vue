<template>
  <div>
   <ul>
      <li v-for="(review,idx) in reviews" :key="idx"> 
        {{ review.content }}

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