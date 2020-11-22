<template>
  <div>
    <h1>글 상세보기</h1>
    <div>
      <p>No : {{board.id}}</p>
      <p>제목 : {{board.title}}</p>
      <p>내용 : {{board.content}}</p>
      <!-- <p>작성자 : {{board.user.username}}}</p>  -->
      <!--위와 같이 쓰면 타입을 undefined으로 인식해 오류가 날 때가 있으므로 주의  -->
      <p>작성자 : {{boardUsername}}</p>
      <p>작성일 : {{ $moment(board.created_at).format('YYYY-MM-DD hh:mm:ss') }}</p>
      <p>수정일 : {{ $moment(board.updated_at).format('YYYY-MM-DD hh:mm:ss') }}</p>
    </div>
    <div>
      <button @click="backToBoard">목록</button>
    </div>
    <br>
    <div>
      <!--작성자와 접속자가 같다면, 수정/삭제 버튼 활성화-->
      <!--단, 관리자의 경우 삭제 버튼 활성화 -->
      <button v-if="boardUsername === this.$store.state.username" @click="updateBoard(board)">글 수정</button>

      <button v-if="this.$store.state.is_admin" @click="deleteBoard(board)">글 삭제</button>
      <button v-else-if="boardUsername === this.$store.state.username" @click="deleteBoard(board)">글 삭제</button>
    </div>
    <hr :style="{'margin':'5px 30px'}">
    <div>
      <CommentForm v-if="this.$store.state.login" :board="board" />
      <p v-else>댓글을 작성하려면 로그인이 필요합니다. </p>
    </div>
    <div>
      <h3>댓글 목록</h3>
      <CommentList :board="board" :comments="all_comments" />
    </div>
  </div>


</template>

<script>
  const SERVER_URL = process.env.VUE_APP_SERVER_URL
  import axios from 'axios'

  import CommentList from '@/components/comment/CommentList'
  import CommentForm from '@/components/comment/CommentForm'

  export default {
    name: 'MovieDetail',
    components: {
      CommentList,
      CommentForm,
    },
    data: function () {
      return {
        board: '',
        boardUsername: '',
        boardItem: '',
        all_comments: '',

      }
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
      backToBoard: function () {
        this.$router.push({
          name: 'Board'
        })
      },
      deleteBoard: function (board) {
        const config = this.setToken()
        axios.delete(`${SERVER_URL}/community/board_delete_update/${board.id}/`, config)
          .then(() => {
            this.$router.push({
              name: 'BoardDetail'
            })
          })
          .catch((err) => {
            console.log(err)
          })
      },
      updateBoard: function (board) {
        const boardItem = {
          id: board.id,
          purpose: 'update',
          title: board.title,
          content: board.content
        }
        this.$router.push({
          name: 'CreateBoard',
          params: boardItem
        })
        //console.log(board.id)

      },
      getAllComment: function () {
        axios.get(`${SERVER_URL}/community/${this.boardItem}/comments/`)
          .then((res) => {
            if (res.data) {
              this.$store.state.comments = res.data
              this.all_comments = this.$store.state.comments
            }
          })
          .catch((err) => {
            console.log(err)
          })
      },

    },
    created: function () {
      this.boardItem = this.$route.params.id
      console.log(this.boardItem)
      axios.get(`${SERVER_URL}/community/${this.boardItem}`)
        .then((res => {
          this.board = res.data
          this.boardUsername = this.board.user.username

        }))
        .catch((err) => {
          console.log(err)
        })

      this.getAllComment()

    }


  }
</script>

<style>

</style>