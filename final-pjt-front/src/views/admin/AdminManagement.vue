<template>
  <div>
    <h1>회원관리 페이지</h1>
    <ul>
      <li v-for="(member,idx) in members" :key="idx">{{ member.username }}</li>
    </ul>

  </div>
</template>

<script>

const SERVER_URL = process.env.VUE_APP_SERVER_URL
import axios from 'axios'

export default {
  name: 'AdminManagement',
  data: function () {
    return {
      members: [],
      admin_info: {
        username : this.$store.state.username
      }


    }
  },
  created: function () {
    axios.post(`${SERVER_URL}/accounts/manage_members/`, this.admin_info)
    .then((res => {
      this.members = res.data
      console.log(this.members)

    }))
    .catch((err) => {
      console.log(err)
    })




    //this.movies = this.$store.state.movie_list

    // console.log(this.movies)

  }
  
}
</script>

<style>

</style>