<template>
  <div>
    <h1>Signup</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input 
        type="password" 
        id="passwordConfirmation" 
        v-model="credentials.passwordConfirmation"
        @keypress.enter="signup"
      >
    </div>
  <div>
      <label for="email">이메일: </label>
      <input type="email" id="email" v-model="credentials.email">
    </div>

    <div>
      <label for="date_of_birth">생년월일: </label>
      <input type="date" id="date_of_birth" v-model="credentials.date_of_birth">
    </div>


    <button @click="signup">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'

//const SERVER_URL = process.env.VUE_APP_SERVER_URL
const SERVER_URL="http://127.0.0.1:8000"

export default {
  name: 'Singup',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        email: '',
        date_of_birth: '',

      }
    }
  },
  methods: {
    signup: function () {
      axios.post(`${SERVER_URL}/accounts/signup/`, this.credentials)
        .then((res) => {
          console.log(res)
          this.$router.push({ name: 'Login' })
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>
