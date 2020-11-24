<template>
  <div>
    <div class="container">
      <div class="row">
        <h1 class="font-do my-3">회원 목록</h1>
        <table class="table table-hover table-dark">
          <thead>
            <tr>
              <th>회원코드</th>
              <th>아이디</th>
              <th>가입일</th>
              <th>생일</th>
              <th>이메일</th>
              <th>등급</th>
              <th>관리</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(member,idx) in members" :key="idx">
              <th>{{ member.id }}</th>
              <th>{{ member.username }}</th>
              <th>{{ $moment(member.date_joined).format('YYYY-MM-DD') }}</th>
              <th>{{ member.date_of_birth }}</th>
              <th>{{ member.email }}</th>
              <th v-if="member.is_superuser">관리자</th>
              <th v-else>일반회원</th>
              <th v-if="member.is_superuser"></th>
              <th v-else><button @click="deleteMember(member)" class="btn btn-danger">삭제</button></th>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
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
          username: this.$store.state.username
        }
      }
    },
    methods: {
      deleteMember: function (member) {

        if (confirm("이 회원을 삭제하겠습니까?")) {
          axios.post(`${SERVER_URL}/accounts/delete_members/${member.id}/`, this.admin_info)
            .then((res) => {
              console.log(res)
              const targetMemberIdx = this.members.findIndex((member) => {
                return member.id === res.data.who
              })
              this.members.splice(targetMemberIdx, 1)
  
            })
            .catch((err) => {
              console.log(err)
            })
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
  @import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&family=Jua&family=Poor+Story&family=Slabo+27px&display=swap');
</style>