<template>
  <div>
    <h1 v-if="this.purpose == 'create'">글 작성하기</h1>
    <h1 v-else-if="this.purpose == 'update'">글 수정하기</h1>

    <div>

      <form v-if="this.purpose == 'create'" v-on:submit.prevent="createBoardForm">
        <div>
          <label for="title">Title: </label>
          <input type="text" id="title" v-model.trim="title" >
        </div>
        <div>
          <label for="content">Content: </label>
          <input type="text" id="content" v-model="content">
        </div>
        <button type="submit">등록하기</button>
      </form>

      <form v-if="this.purpose == 'update'" v-on:submit.prevent="updateBoard">
        <div>
          <label for="title">Title: </label>
          <input type="text" id="title" v-model.trim="title">
        </div>
        <div>
          <label for="content">Content: </label>
          <input type="text" id="content" v-model="content">
        </div>
        <button type="submit">등록하기</button>
      </form>
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
        title: '',
        content: '',
        purpose: '',
        updateId:'', 
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
      createBoardForm: function () {
        const config = this.setToken()

        const boardItem = {
          title: this.title,
          content: this.content
        }
        axios.post(`${SERVER_URL}/community/board_create/`, boardItem, config)
          .then((res) => {
            //console.log(res)
            this.$router.push({
              name: 'BoardDetail',
              params: {
                'id': res.data.id
              }
            })
          })
          .catch((err) => {
            console.log(err)
          })
      },
      updateBoard: function () {
        const config = this.setToken()

        const boardItem = {
          title: this.title,
          content: this.content,
          board_code: 1,
        }
        axios.put(`${SERVER_URL}/community/board_delete_update/${this.updateId}/`, boardItem, config)
          .then((res) => {
            //console.log(res)
            this.$router.push({
              name: 'BoardDetail',
              params: {
                'id': res.data.id
              }
            })
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
    created: function () {
      this.purpose = this.$route.params.purpose
      this.updateId = this.$route.params.id
      this.title = this.$route.params.title
      this.content = this.$route.params.content
    
    }

  }
</script>

<style>

</style>