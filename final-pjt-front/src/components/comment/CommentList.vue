<template>
  <div>
    
    <h2 class="mt-5 font-do">댓글 목록</h2>

    <div v-for="(comment, idx) in comments" :key="idx" class="media mt-3">
      <a class="mr-3" href="#">
        <img :src="images.flamingo" width="50" class="mr-1" alt="...">
      </a>
      <div class="media-body">
        <h3 class="mt-0">[{{comment.user.username}}] {{comment.content}} </h3>
        <p>작성: {{ $moment(comment.created_at).format('YYYY-MM-DD hh:mm:ss') }}  |</p>
        <p>수정: {{ $moment(comment.created_at).format('YYYY-MM-DD hh:mm:ss') }}</p>
      <div v-if="updateTrigger === comment.id">
        <UpdateForm :updateCommentItem="updateCommentItem" :board="board" @trigger="changeTrigger" />
      </div>
      <div>
        <!--작성자와 접속자가 같다면, 수정/삭제 버튼 활성화-->
        <!--단, 관리자의 경우 삭제 버튼 활성화 -->
        <button class="btn btn-pink mr-1" v-if="comment.user.id === login_user && updateTrigger === false" @click="updateBoardForm(comment)">댓글
          수정</button>

        <button class="btn btn-secondary font-jua mr-1" v-if="is_admin && updateTrigger === false" @click="deleteComment(comment)">댓글 삭제</button>
        <button class="btn btn-secondary font-jua mr-1 " v-else-if="comment.user.id === login_user && updateTrigger === false" @click="deleteComment(comment)">댓글
          삭제</button>

      </div>
      </div>
    </div>


    <!-- <h5 class="mt-0">Media heading</h5>
    <div v-for="(comment, idx) in comments" :key="idx">
      <hr>
      <p>[{{comment.user.username}}]</p>
      <p>{{comment.content}}</p>
      <p>{{ $moment(comment.created_at).format('YYYY-MM-DD hh:mm:ss') }}</p>
      <p>{{ $moment(comment.created_at).format('YYYY-MM-DD hh:mm:ss') }}</p>
      <div v-if="updateTrigger === comment.id">
        <UpdateForm :updateCommentItem="updateCommentItem" :board="board" @trigger="changeTrigger" />
      </div>
      <div>
 
        <button v-if="comment.user.id === login_user && updateTrigger === false" @click="updateBoardForm(comment)">댓글
          수정</button>

        <button v-if="is_admin && updateTrigger === false" @click="deleteComment(comment)">댓글 삭제</button>
        <button v-else-if="comment.user.id === login_user && updateTrigger === false" @click="deleteComment(comment)">댓글
          삭제</button>

      </div>

      <hr>
    </div> -->
  </div>
</template>


<script>
  const SERVER_URL = process.env.VUE_APP_SERVER_URL
  import axios from 'axios'
  import UpdateForm from '@/components/comment/UpdateForm'

  import {
    mapState
  } from 'vuex'

  export default {
    name: 'CommentList',
    components: {
      UpdateForm,
    },
    data: function () {
      return {
        updateTrigger: false,
        updateCommentItem: '',
        images: {
          logo: require('@/assets/images/logo.png'),
          flamingo: require('@/assets/images/flamingo.png')

        },

      }
    },
    props: {
      board: [Object, String],
    },
    methods: {
      setToken: function () {
        const token = localStorage.getItem('jwt')

        const config = {
          headers: {
            Authorization: `JWT ${token}`
          }
        }
        return config
      },

      deleteComment: function (comment) {
        const config = this.setToken()
        axios.delete(`${SERVER_URL}/community/${this.board.id}/comment/${comment.id}/`, config)
          .then((res) => {
            //console.log(res)
            const targetCommentIdx = this.comments.findIndex((comment) => {
              return comment.id === res.data.id
            })
            this.$store.state.comments.splice(targetCommentIdx, 1)
          })
          .catch((err) => {
            console.log(err)
          })
      },
      updateBoardForm: function (comment) {
        this.updateTrigger = comment.id
        this.updateCommentItem = comment

        // const boardItem = {
        //   id: board.id,
        //   purpose: 'update',
        //   title: board.title,
        //   content: board.content
        // }
        // this.$router.push({
        //   name: 'CreateBoard',
        //   params: boardItem
        // })
        //console.log(board.id)

      },
      changeTrigger: function () {
        this.updateTrigger = false
      }

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
        'is_admin',
        'comments',
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