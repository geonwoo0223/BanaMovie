<template>
  <div>
    <form v-on:submit.prevent="updateComment">
      <div id="updateDiv">
        <label for="content">Content: </label>
        <input type="text" id="content" v-model="content">
      </div>
      <button type="submit" @click="updateComment(board)">수정완료</button>
    </form>
  </div>
</template>

<script>
    const SERVER_URL = process.env.VUE_APP_SERVER_URL
    import axios from 'axios'

  export default {
    name: 'UpdateForm',
    data: function () {
      return {
        content: '',
        comments: '',
      }
    },
    props: {
      updateCommentItem: [Object, String],
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
      updateComment: function () {
        const config = this.setToken()
        const updateItem = {
          ...this.updateCommentItem,
          board : this.board.id,
          content : this.content
        }
        axios.put(`${SERVER_URL}/community/${this.board.id}/comment/${this.updateCommentItem.id}/`,updateItem, config)
        .then( (res) => {
          console.log(res)
          this.$emit("trigger")
          const targetCommentIdx = this.comments.findIndex((comment) => {
            return comment.id === res.data.id
          })
          this.$store.state.comments[targetCommentIdx].content = this.content

          
        })
        .catch( (err) => {
          console.log(err)
        })


      },
    },
    created: function () {
      this.content = this.updateCommentItem.content
      this.comments = this.$store.state.comments
    },
  }
</script>

<style scoped>
  #updatedDiv {
    display: inline;
  }

  form {
    display: inline;
  }
</style>