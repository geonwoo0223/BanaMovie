<template>
  <div>
      <div id="commentdiv" v-for="(comment, idx) in comments" :key="idx">
          <hr>
          <p>[{{comment.user.username}}]</p>
          <p>{{comment.content}}</p>
          <p>{{ $moment(comment.created_at).format('YYYY-MM-DD hh:mm:ss') }}</p>
          <p>{{ $moment(comment.created_at).format('YYYY-MM-DD hh:mm:ss') }}</p>
          <button>수정</button>
          <button>삭제</button>
          <hr>
      </div>
  </div>
</template>


<script>
import { mapState } from 'vuex'

export default {
    name: 'CommentList',
    data: function () {
        return {

        }
    },
    props: {
        board: Object,
        comments: [Array, String],
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

<style scoped>

div > p {
    display: inline;
    margin : 10px 5px;
}

</style>