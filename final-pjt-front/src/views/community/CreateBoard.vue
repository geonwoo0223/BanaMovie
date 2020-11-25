<template>
  <div>
    <h1 v-if="this.purpose == 'create'" class="font-do my-3">글 작성하기</h1>
    <h1 v-else-if="this.purpose == 'update'" class="font-do my-3">글 수정하기</h1>

    <div class="container">

      <div class="row">

      <form v-if="this.purpose == 'create'" v-on:submit.prevent="createBoardForm"
      class="font-poor font-1-2em">
        <div class="form-group row">
          <label class="col-sm-3 col-form-label" for="title">Title: </label>
          <div class="col-sm-9">
            <input type="text" class="form-control" id="title" v-model.trim="title">
          </div>
        </div>

        <div class="form-group row">
          <label for="content" class="col-sm-3 col-form-label">Content: </label>
          <div class="col-sm-9">
          <textarea class="form-control" id="content" v-model="content"></textarea>
          </div>
        </div>
        <button type="submit" class="btn btn-pink">등록하기</button>
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
        updateId: '',
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
            alert("잘못된 정보를 입력했습니다.")
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