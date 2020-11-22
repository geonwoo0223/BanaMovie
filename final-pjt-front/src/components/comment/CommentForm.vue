<template>
  <div>
    <form v-on:submit.prevent="createComment">
      <div>
        <label for="content">Content: </label>
        <input type="text" id="content" v-model="content">
      </div>
      <button type="submit">댓글등록</button>
    </form>
  </div>
</template>

<script>
  const SERVER_URL = process.env.VUE_APP_SERVER_URL
  import axios from 'axios'

  export default {
    name: 'CommentForm',
    data: function () {
      return {
        content: '',
      }
    },
    props: {
      board: Object,
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
      createComment: function () {
        const config = this.setToken()

        const commentItem = {
          content: this.content
        }
        //console.log(this.board)
        const boardId = this.board.id
        axios.post(`${SERVER_URL}/community/${boardId}/comment_create/`, commentItem, config)
          .then((res) => {
            console.log(res)
            this.content = ''
          })
          .catch((err) => {
            console.log(err)
          })
      },
    }
  }
</script>

<style>

</style>