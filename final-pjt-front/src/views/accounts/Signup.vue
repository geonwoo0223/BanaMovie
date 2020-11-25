<template>
  <div class="container">
    
    <h1 class="font-do my-3">Sign up</h1>
  
      <div class="form-group mt-5 font-poor font-1-2em">
      <label for="username" >사용자 이름: </label>   
      <input type="text" class="form-control" id="username" v-model="credentials.username">
      </div>

    <div class="form-group mt-5 font-poor font-1-2em">
      <label for="password">비밀번호: </label>
      <input type="password" class="form-control" id="password" v-model="credentials.password">
    </div>
    <div class="form-group mt-5 font-poor font-1-2em">
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input 
        type="password" 
        id="passwordConfirmation" 
        v-model="credentials.passwordConfirmation"
        @keypress.enter="signup"
        class="form-control"
      >
    </div>
  <div class="form-group mt-5">
      <label for="email">이메일: </label>
      <input type="email" class="form-control" id="email" v-model="credentials.email">
       <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>

    </div>

    <div class="form-group mt-5 font-poor font-1-2em">
      <label for="date_of_birth">생년월일: </label>
      <input type="date" class="form-control" id="date_of_birth" v-model="credentials.date_of_birth">
    </div>

    <div class="form-group mt-3 float-left">
    <div class="form-check">
      <input class="form-check-input" type="checkbox" id="gridCheck" v-model="agree">
      <label class="form-check-label" for="gridCheck">
        개인정보 이용 약관에 동의합니다.
      </label>
    </div>
  </div>
  <br>


    <button @click="signup" id="signupbtn" class="btn btn-pink my-5">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Singup',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        email: '',
        date_of_birth: '',
        agree: false,

      }
    }
  },
  methods: {
    signup: function () {
      if (this.agree === true) {
        axios.post(`${SERVER_URL}/accounts/signup/`, this.credentials)
          .then((res) => {
            console.log(res)
            this.$router.push({ name: 'Login' })
          })
          .catch((err) => {
            console.log(err)
            alert("회원가입 정보가 틀렸습니다.")
          })
      } else {
        alert("개인정보 이용 약관에 동의해야합니다.")
      }
    }
  }
}
</script>

<style scoped>
#signupbtn{
  font-size: 2em !important;
  width:200px !important;
}

</style>
