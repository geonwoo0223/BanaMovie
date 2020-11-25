<template>
  <div>
    <div class="container">
      <div class="row">
        <h1 class="font-do mt-5">Hello! :)</h1>
      </div>
      <div class="row">
        <div class="col-6" id="rightline">
          <div class="card text-white bg-dark mb-3 mt-5" style="max-width: 18rem;">
            <h2 class="card-header font-do">로그인</h2>
            <div class="card-body">
              <div class="input-group-lg">
              <h4 class="card-title font-do">아이디</h4>
              <input type="text" id="username" class="font-poor form-control" v-model="credentials.username">
              </div>
              <br>
              <br>
              <div class="input-group-lg">
              <h4 class="card-title font-do">비밀번호</h4>
              <input type="password" id="password" class="font-poor form-control" v-model="credentials.password" @keypress.enter="login">
              </div>
              <br>
              <button @click="login" class="btn btn-pink mt-3 font-1-5em btn-block">로그인</button>
            </div>

          </div>
        </div>

      <div class="col-6 d-flex align-items-center justify-content-center">
        <div>
        <h3 class="font-do">잠깐! :0 아직 회원이 아니신가요?</h3>
        <div class="emptydiv"></div>
        <router-link :to="{ name: 'Signup' }" class="btn btn-block btn-pink mr-auto nav-margin font-1-5em">회원 가입 하러가기</router-link>
        <div class="emptydiv"></div>
        </div>
      </div>

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
                this.$store.state.username = this.credentials.username
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
            alert("로그인 정보가 일치하지 않습니다.")
          })
      }
    },
    created: function () {

    }
  }
</script>

<style scoped>

#rightline{

  border-right: dotted grey;
}

.emptydiv{
  height: 50px;
}

</style>