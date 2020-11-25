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
        <input class="form-check-input" type="checkbox" id="gridCheck" checked="true" v-model="agree">
        <label class="form-check-label" for="gridCheck">
          <p @click="agreePage">개인정보 이용 약관에 동의합니다.</p>
        </label>
      </div>
    </div>
  <br>

    <div class="form-group mt-5 font-poor font-1-2em">
      <button @click="signup" id="signupbtn" class="btn btn-pink my-5 form-group">회원가입</button>
    </div>

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
      },
      agree: false,
    }
  },
  methods: {
    signup: function () {
      if (this.agree === true) {
        axios.post(`${SERVER_URL}/accounts/signup/`, this.credentials)
          .then((res) => {
            console.log(res)
            this.$router.push({ name: 'Login' })
            this.agree = false
          })
          .catch((err) => {
            console.log(err)
            alert("회원가입 정보가 틀렸습니다.")
          })
      } else {
        alert("개인정보 이용 약관에 동의해야합니다.")
      }
    },
    agreePage: function () {
      alert("① 정보주체는 DeJaVue에 대해 언제든지 개인정보 열람,정정,삭제,처리정지 요구 등의 권리를 행사할 수 있습니다. \n② 제1항에 따른 권리 행사는DeJaVue에 대해 개인정보 보호법 시행령 제41조제1항에 따라 서면, 전자우편, 모사전송(FAX) 등을 통하여 하실 수 있으며 DeJaVue은(는) 이에 대해 지체 없이 조치하겠습니다. \n③ 제1항에 따른 권리 행사는 정보주체의 법정대리인이나 위임을 받은 자 등 대리인을 통하여 하실 수 있습니다. 이 경우 개인정보 보호법 시행규칙 별지 제11호 서식에 따른 위임장을 제출하셔야 합니다. \n④ 개인정보 열람 및 처리정지 요구는 개인정보보호법 제35조 제5항, 제37조 제2항에 의하여 정보주체의 권리가 제한 될 수 있습니다. \n⑤ 개인정보의 정정 및 삭제 요구는 다른 법령에서 그 개인정보가 수집 대상으로 명시되어 있는 경우에는 그 삭제를 요구할 수 없습니다. \n⑥ DeJaVue은(는) 정보주체 권리에 따른 열람의 요구, 정정·삭제의 요구, 처리정지의 요구 시 열람 등 요구를 한 자가 본인이거나 정당한 대리인인지를 확인합니다.")
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
