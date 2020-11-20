<template>
  <div>
    <h1>Login</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input 
        type="password" 
        id="password" 
        v-model="credentials.password"
        @keypress.enter="login"
      >
    </div>
    <button @click="login">로그인</button>
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
    login: function () {
      axios.post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
        .then((res) => {
          // console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$store.state.login = true
          // console.log(res)

          axios.post(`${SERVER_URL}/accounts/is-admin/`, this.credentials)
          .then((res) => {
            // console.log(res)
            this.$store.state.is_admin = res.data
          })
          .catch((err) => {
            console.log(err)
          })

          this.$router.push({ name: 'MovieList' })
          this.$store.state.username = this.credentials.username
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>
