<template>
  <div>

    <div class="card text-white bg-dark mb-3 mt-5" style="max-width: 18rem;">
      <h2 class="card-header font-do">로그인</h2>
      <div class="card-body">
        <h5 class="card-title">아이디</h5>
        <input type="text" id="username" v-model="credentials.username">
      <br>
      <br>
      <h5 class="card-title">비밀번호</h5>
      <input type="password" id="password" v-model="credentials.password" @keypress.enter="login">
      <br>
      <button @click="login" class="btn btn-pink">로그인</button>
    </div>



  
   
  </div>
  </div>
</template>

<script>
  import axios from 'axios'

  const SERVER_URL = process.env.VUE_APP_SERVER_URL

  export default {
    name: 'Login',
    data: function () {
      return {
        credentials: {
          username: '',
          password: '',
        }
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

      login: function () {
        axios.post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
          .then((res) => {
            // console.log(res)
            localStorage.setItem('jwt', res.data.token)
            this.$emit('login')
            this.$store.state.login = true

            // console.log(res)
            const config = this.setToken()
            axios.get(`${SERVER_URL}/accounts/user/`, config)
              .then((res) => {
                // console.log(res.data)
                const id = res.data
                this.$store.state.login_user = id
                this.$store.dispatch('recommendMovie', id)
                // console.log(this.$store.state.login_user)
              })
              .catch((err) => {
                console.log(err)
              })

            axios.post(`${SERVER_URL}/accounts/is-admin/`, this.credentials)
              .then((res) => {
                this.$store.dispatch('isAdmin', res.data)
              })
              .catch((err) => {
                console.log(err)
              })
            this.$store.state.username = this.credentials.username
            if (this.flag) {
              this.$router.push({
                name: 'AdminManagement'
              })
            } else {
              this.$router.push({
                name: 'MovieList'
              })
            }
          })
          .catch((err) => {
            console.log(err)
            alert("로그인 정보가 틀렸습니다.")
          })
      }
    },
    created: function () {

    }
  }
</script>

<style scoped>
  
</style>