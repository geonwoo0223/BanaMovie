<template>
  <div>
    <form v-on:submit.prevent="updateComment">
      <div id="updateDiv">
        <label for="content">Content: </label>
        <input type="text" id="content" v-model="content">
      </div>
      <button type="submit">수정완료</button>
    </form>
  </div>
</template>

<script>
//   const SERVER_URL = process.env.VUE_APP_SERVER_URL
//   import axios from 'axios'

  export default {
    name: 'UpdateForm',
    data: function () {
      return {
        content: '',
      }
    },
    // props: {
    //   updateCommentItem: [Object, String],
    // },
    // methods: {
    //   setToken: function () {
    //     const token = localStorage.getItem('jwt')

    //     const config = {
    //       headers: {
    //         Authorization: `JWT ${token}`
    //       }
    //     }
    //     return config
    //   },
    //   updateComment: function () {
    //     const config = this.setToken()

    //     const commentItem = {
    //       content: this.content
    //     }
    //     //console.log(this.board)
    //     const boardId = this.board.id
    //     axios.delete(`${SERVER_URL}/community/${boardId}/comment/${comment.id}`, commentItem, config)
    //       .then((res) => {
    //         console.log(res)
    //         // this.$store.state.comments.unshift(res.data)
    //         // this.content = ''
    //       })
    //       .catch((err) => {
    //         console.log(err)
    //       })
    //   },
  
    //},
    created: function () {
    //console.log(typeof(this.board))
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