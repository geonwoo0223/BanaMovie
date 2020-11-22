<template>
  <div>
    <div id="commentdiv" v-for="(comment, idx) in comments" :key="idx">
      <hr>
      <p>[{{comment.user.username}}]</p>
      <p>{{comment.content}}</p>
      <p>{{ $moment(comment.created_at).format('YYYY-MM-DD hh:mm:ss') }}</p>
      <p>{{ $moment(comment.created_at).format('YYYY-MM-DD hh:mm:ss') }}</p>
      <div>
        <!--작성자와 접속자가 같다면, 수정/삭제 버튼 활성화-->
        <!--단, 관리자의 경우 삭제 버튼 활성화 -->
        <button v-if="comment.user.id === login_user" >댓글 수정</button>

        <button v-if="is_admin" >댓글 삭제</button>
        <button v-else-if="comment.user.id === login_user" >댓글 삭제</button>
        <!-- <button >글 수정</button>

        <button >글 삭제</button> -->
      </div>
      <hr>
    </div>
  </div>
</template>


<script>
  import {
    mapState
  } from 'vuex'

  export default {
    name: 'CommentList',
    data: function () {
      return {
        // username:'',
        // login:''
        

      }
    },
    props: {
      board: [Object, String],
      comments: [Array, String],
    },
    created: function () {
      // if (login) {
      //   this.username = this.$store.state.username
      //   this.login = this.$store.state.login
      // }
      
    },
    computed: {
      ...mapState([
        'login',
        'login_user',
        'username',
        'is_admin'
      ])
    }


  }
</script>

<style scoped>
  div>p {
    display: inline;
    margin: 10px 5px;
  }
</style>