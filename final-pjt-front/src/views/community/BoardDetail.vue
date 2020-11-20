<template>
<div>
  <h1>글 상세보기</h1>
  <div>
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
    <button v-if="boardUsername === this.$store.state.username">글 수정</button>

    <button v-if="this.$store.state.is_admin">글 삭제</button>
    <button v-else-if="boardUsername === this.$store.state.username">글 삭제</button>
  </div>
</div>

  
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL
import axios from 'axios'

export default {
  name: 'MovieDetail',
  data: function () {
      return {
        board: '',
        boardUsername:'',
        boardItem: '',
        
    }
  },
  methods: {
    backToBoard: function () {
      this.$router.push({name:'Board'})
    }
  },
  created: function() {
    this.boardItem = this.$route.params.id
    //console.log(this.boardItem)
    axios.get(`${SERVER_URL}/community/${this.boardItem}`)
    .then((res => {
      this.board = res.data
      //console.log(this.board)
      //console.log(typeof(this.board.user.username))
      this.boardUsername = this.board.user.username

    }))
    .catch((err) => {
      console.log(err)
    })

  }
  

}
</script>

<style>

</style>