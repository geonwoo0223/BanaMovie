<template>
  <div>
      <h1>글 작성하기</h1>
      <form v-on:submit.prevent="createBoard">
      <div>
      <label for="title" >Title: </label>
      <input type="text" id="title" v-model.trim="title">
        </div>
        <div>
      <label for="content">Content: </label>
      <input type="text" id="content" v-model="content">
    </div>
    <button type="submit">등록하기</button>
    </form>
    
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
      title:'',
      content:'', 
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
        const config = this.setToken()

        const boardItem = {
            title: this.title,
            content: this.content
        }
        axios.post(`${SERVER_URL}/community/`,boardItem, config)
        .then( (res) => {
          //console.log(res)
          this.$router.push({ name: 'BoardDetail', params:{'id':res.data.id} })
          
          
        })
        .catch( (err) => {
          console.log(err)
        })
    }
  },
  created: function () {
    

  }

}
</script>

<style>

</style>