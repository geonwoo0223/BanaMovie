<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-3">
          <h1 class="font-do my-3">게시판</h1>
        </div>
        <div class="col-9 align-middle">
          
          <button v-if="this.$store.state.login" @click="createBoard()" class="btn btn-pink font-1-5em my-4">글 작성하기</button>
          <p v-else class="my-4 float-right">게시글을 작성하려면 로그인이 필요합니다.</p>
    
        </div>
      </div>
      <div class="row">
        <table class="table table-hover table-dark">
          <tr>
            <th>No</th>
            <th>제목</th>
            <th>작성자</th>
            <th>작성일</th>
          </tr>
          <tr v-for="(board,idx) in boards" :key="idx">
            <th>{{ board.id }}</th>
            <!-- <th><a v-on:click.stop="boardDetail(board)">{{ board.title }}</a></th> -->
            <th @click="boardDetail(board)">{{ board.title }}</th>
            <th>{{ board.user.username }}</th>
            <th>{{ $moment(board.created_at).format('YYYY-MM-DD hh:mm:ss') }}</th>
          </tr>
        </table>

      </div>
    </div>
  </div>
</template>

<script>
  const SERVER_URL = process.env.VUE_APP_SERVER_URL
  import axios from 'axios'

  export default {
    name: 'Board',
    data: function () {
      return {
        boards: [],
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
      createBoard: function () {
        this.$router.push({
          name: 'CreateBoard',
          params: {
            'purpose': 'create'
          }
        })
      },
      boardDetail: function (board) {
        this.$router.push({
          name: 'BoardDetail',
          params: {
            'id': board.id
          }
        })

      }

    },
    created: function () {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/community/`, config)
        .then((res => {
          this.boards = res.data
          //console.log(this.boards)

        }))
        .catch((err) => {
          console.log(err)
        })

    },
    mounted() {
      window.scrollTo(0,0)
    }

  }
</script>

<style>

</style>