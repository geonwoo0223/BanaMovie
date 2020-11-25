<template>
  <div class="col-3">
    
    <button>
      <img @click="showDetail" :src="movie.poster_path" :alt="movie.title" v-if="!movie.poster_path.includes('#')"/>
      <img @click="showDetail" src="https://image.tmdb.org/t/p/w185/g3gpHLUuQLGI9gRmfraSQCN1TYk.jpg" :alt="movie.title" v-else/>
    </button>


    <!-- 영화눌렀을때 이게 보이게 한다 -->
    <b-modal class="font-do" hide-footer v-model="show" size="lg" title="Movie information" header-bg-variant="dark"
      header-text-variant="light" body-bg-variant="dark" body-text-variant="light" footer-bg-variant="dark"
      footer-text-variant="dark">
      <!-- 영화디테일 부분 -->
      <div class="detail-box">
        <img :src="movie.poster_path" alt="movie poster" id="movie-poster" v-if="!movie.poster_path.includes('#')">
        <img src="https://image.tmdb.org/t/p/w185/g3gpHLUuQLGI9gRmfraSQCN1TYk.jpg" alt="movie poster" id="movie-poster" v-else/>
        <h2 class="font-do">{{ movie.title }}</h2>
        <h5 class="font-do">{{ movie.release_date }}</h5>
        <h5 class="font-do" v-if="movie.adult">19세 관람가</h5>
        <br />
        <h4 class="font-poor">줄거리: {{ movie.overview | truncate(100, '...') }}</h4>
        <h4 class="font-poor">평점: {{ movie_list[movie.id]["rate"] }}</h4>
        <hr />
      </div>
      <br>



      <!-- 리뷰부분 -->
      <div v-if="is_admin === false && login === true" :class="{ appear: showForm }">
        <h2 class="font-do">리뷰 작성하기</h2>
        <div id="reviewForm">
          <div>

            <label for="rate" class="float-left font-jua font-1-5em ">별점</label>
            <p class="float-left font-jua font-1-5em mr-3">: {{ selected_rate }}점</p>
            <input type="range" min="1" max="10" step="1" v-model="selected_rate" class="mt-2 justify-content-center">
            <select id="rate" v-model="selected_rate" class="ml-1">
              <option v-for="(n, idx) in rate_options" :key="idx">{{n}}</option>
            </select>

            <b-input-group>
              <b-input-group-prepend>
                <b-button @click="selected_rate = null">Clear</b-button>
              </b-input-group-prepend>
              <b-form-rating size="lg" id="rate" v-model="selected_rate" color="#DE5078" stars="10"></b-form-rating>
              <b-input-group-append>
                <b-input-group-text class="justify-content-center" style="min-width: 3em;">
                  {{ selected_rate }}
                </b-input-group-text>
              </b-input-group-append>
            </b-input-group>
          </div>
          <div class="mt-3">
            <label for="like" class="mr-2 font-jua font-1-5em mr-1">이 영화를</label>
            <label for="like" class="font-jua font-1-5em mr-2" id="recommend-label">추천합니다.</label>
            <b-form-checkbox size="lg" id="like" checked="true" v-model="like" inline></b-form-checkbox>
          </div>


          <div class="input-group">
            <label for="content"></label>
            <textarea class="form-control my-3 font-poor" aria-label="With textarea" id="content" cols="60" rows="5"
              v-model.trim="content" placeholder="감상평을 남겨주세요."></textarea>
          </div>



          <div>
            <div class="d-flex justify-content-center">
              <button @click="hideDetail" class="btn btn-secondary font-jua mr-1 ml-1">취소</button>
              <button :class="{ appear: showAdd }" class="btn btn-pink mr-1 ml-1" @click="addReview(movie)">확인</button>
              <button :class="{ appear: !showAdd }" class="btn btn-pink font-jua mr-1 ml-1"
                @click="updateReview(movie)">수정</button>
            </div>
          </div>
        </div>
      </div>

      <!-- 리뷰목록 -->

      <h2 class="font-do">리뷰 목록</h2>
      <hr>
      <ul>


        <li v-for="(review,idx) in review_list" :key="idx">
          <div v-if="review.movie.id === movie.id || review.id === movie.id">
            <div class="row review-dottedline mt-5">


              <div class="col-3" id="review-rank">
                <div>
                  <b-form-rating color="#DE5078" inline size="sm" :value="review.rate | half() " readonly no-border>
                  </b-form-rating>
                </div>
              </div>

              <div class="col-6" id="review-content">
                <p>{{ review.content }}</p>
                <p>작성자 : {{ review.user.username }} | {{$moment(review.created_at).format('YYYY-MM-DD')}} </p>
              </div>

              <div class="col-3" id="review-button" v-if="review.user.id === login_user">
                <button @click="updateReady(review)" class="btn btn-pink mr-1 ml-1">수정</button>
                <button @click="deleteReview(movie)" class="btn btn-delete mr-1 ml-1">삭제</button>
              </div>

            </div>
          </div>
        </li>



      </ul>
    </b-modal>

  </div>
</template>

<script>
  const SERVER_URL = process.env.VUE_APP_SERVER_URL

  import axios from 'axios'
  import _ from 'lodash'
  import {
    mapState
  } from 'vuex'



  export default {
    name: 'MovieListItem',
    props: {
      movie: Object,
    },
    data: function () {
      return {
        selected_rate: null,
        like: false,
        content: null,
        show: false,
        showForm: false,
        showAdd: false,
        reviewId: null,
        rate_options: _.range(0, 11),
        variants: ["light", "dark"],
      }
    },
    methods: {
      showDetail: function () {
        this.show = true
      },
      hideDetail: function () {
        this.show = false
      },
      setToken: function () {
        const token = localStorage.getItem('jwt')

        const config = {
          headers: {
            Authorization: `JWT ${token}`
          }
        }
        return config
      },
      addReview: function (movie) {
        const config = this.setToken()
        const reviewInfo = {
          content: this.content,
          rate: this.selected_rate,
          like: this.like,
        }

        axios.post(`${SERVER_URL}/movies/${movie.id}/review/`, reviewInfo, config)
          .then((res) => {
            // console.log(res.data)
            const reviewerInfo = {
              movie_id: this.movie.id,
              reviewer_id: res.data.user.id
            }
            this.$store.state.review_list.unshift(res.data)
            let acount = 0
            for (const review of this.review_list) {
              if (review.movie.id === this.movie.id) {
                acount++
              }
            }
            this.total[this.movie.id] += this.selected_rate
            this.$store.state.movie_list[this.movie.id].rate = this.total[this.movie.id]/acount
            this.$store.dispatch('checkReviewer', reviewerInfo)
            this.$store.dispatch('recommendMovie')
            this.content = null
            this.selected_rate = null
            this.like = false
            this.showForm = true
          })
          .catch((err) => {
            console.log(err)
          })
      },
      deleteReview: function (movie) {
        const config = this.setToken()
        if (confirm("이 리뷰를 삭제하겠습니까?")) {
          axios.delete(`${SERVER_URL}/movies/${movie.id}/review/update/`, config)
            .then((res) => {
              console.log(res)
              const idx1 = this.review_list.indexOf(res.data.id)
              this.$store.state.review_list.splice(idx1, 1)

              const idx2 = this.user_movie[this.login_user].indexOf(movie.id)
              this.$store.state.user_movie[this.login_user].splice(idx2, 1)

              let dcount = 0
              for (const review of this.review_list) {
                if (review.movie.id === this.movie.id) {
                  dcount--
                }
              }
              if (dcount === 0) {
                dcount++
              }
              this.total[this.movie.id] -= res.data.rate
              this.$store.state.movie_list[this.movie.id].rate = this.total[this.movie.id]/dcount




              this.showForm = false
              this.showAdd = false
            })
            .catch((err) => {
              console.log(err)
            })
        }

      },
      updateReady: function (review) {
        this.content = review.content
        this.like = review.like
        this.selected_rate = review.rate
        this.showForm = false
        this.showAdd = true
        this.reviewId = review.id
      },

      updateReview: function (movie) {
        const config = this.setToken()
        const reviewInfo = {
          id: this.reviewId,
          user: this.login_user,
          movie: movie.id,
          content: this.content,
          rate: this.selected_rate,
          like: this.like,
        }
        axios.put(`${SERVER_URL}/movies/${movie.id}/review/update/`, reviewInfo, config)
          .then((res) => {
            this.content = null
            this.like = false
            this.selected_rate = null
            this.showForm = true
            this.showAdd = false
            this.reviewId = null
            console.log(res)
            const idx = this.review_list.findIndex((review) => {
              return review.id === res.data.id
            })
            this.total[this.movie.id] -= this.$store.state.review_list[idx].rate
            this.$store.state.review_list[idx].content = res.data.content
            this.$store.state.review_list[idx].rate = res.data.rate
            this.$store.state.review_list[idx].like = res.data.like

            let ucount = 0
            for (const review of this.review_list) {
              if (review.movie.id === this.movie.id) {
                ucount++
              }
            }
            this.total[this.movie.id] += res.data.rate
            this.$store.state.movie_list[this.movie.id].rate = this.total[this.movie.id]/ucount

          })
          .catch((err) => {
            console.log(err)
          })
      },

    },
    created: function () {
      if (this.user_movie[this.login_user] && this.user_movie[this.login_user].includes(this.movie.id)) {
        this.showForm = true
      }
      this.avgRate = this.movie.rate
    },
    computed: {
      ...mapState([
        'login',
        'login_user',
        'is_admin',
        'user_movie',
        'movie_list',
        'review_list',
        'total'
      ]),

    },
  }
</script>

<!--<style scoped src="@/assets/css/mycss.css">-->
<style scoped>


  .appear {
    display: none;
  }

  #movie-poster {
    width: 300px;
    min-height: 400px;
    max-height: 500px;
    float: left;
    margin-right: 20px;
  }

  .detail-box {
    height: 500px;
  }

  #recommend-label:hover {
    color: #DE5078;
  }

  ul {
    list-style: none;
  }


  .review-dottedline {
    border-bottom: 2px dotted gainsboro;

  }

  .btn-delete{
    background-color: gray;
    border: 1px dotted gainsboro;
    color: honeydew;
    font-family: Jua;
  }

  .btn-pink {
    font-family: Jua;
    background-color: #DE5078;
    color: aliceblue;
  }

  .font-jua {
    font-family: 'Jua';
  }

  .font-do {
    font-family: 'Do Hyeon';
  }

  .font-poor {
    font-family: 'Poor Story';
  }

  .font-1em {
    font-size: 1em;
    ;
  }


  .font-2em {
    font-size: 2em;
    ;
  }

  .font-1-2em {
    font-size: 1.2em;
  }

  .font-1-5em {
    font-size: 1.5em;
    ;
  }

  .font-1-8em {
    font-size: 1.8em;
    ;
  }

  #review-rank .form-control {
    background-color:#343a40;
  }
</style>