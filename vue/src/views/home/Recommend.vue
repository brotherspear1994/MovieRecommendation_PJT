<template>
  <div>

    <h2 class="title-font" style="margin-bottom:60px">SSAFLIX 알고리즘이 {{user.username}}님에게 추천하는 영화 페이지</h2>
    <h3 class="content-font" v-if="my_users_like_movies.length > 0">{{user.username}} 님의 취향저격 베스트 콘텐츠</h3>
    <MovieCard :movies="my_users_like_movies"/>
    <h3 class="content-font">랜덤 영화 추천</h3>
    <MovieCard :movies="movies"/>
    <h3 class="content-font" v-if="favorite_movies.length === 30">높은 평점을 받은 영화</h3>
    <MovieCard :movies="favorite_movies"/>
    <h3 class="content-font" v-if="shortest_movies.length === 30">짧은 러닝타임, 가볍게 볼 수 있는 영화</h3>
    <MovieCard :movies="shortest_movies"/>
    <h3 class="content-font" v-if="users_movies.length === 30">SSAFLIX 유저들이 많이 리뷰한 영화</h3>
    <MovieCard :movies="users_movies"/>


  </div>
</template>

<script>

import axios from 'axios'
import _ from 'lodash'
import MovieCard from "@/components/MovieCard"

import VueJwtDecode from "vue-jwt-decode"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "Recommend",
  data: function () {
    return {
      movies: [],
      movie: '',
      favorite_movies: [],
      shortest_movies: [],
      users_movies: [],
      my_like_users_movies: [],
      user: '',
      my_users_like_movies: [],
    }
  },
  components: {
    MovieCard,
  },
  methods: {
    getToken: function () {
      const token = localStorage.getItem('jwt')

      const config = {
        headers: {
          Authorization: `JWT ${token}`
        },
      }
      return config
    },
    getMovieDatas: function () {
      axios.get(`${SERVER_URL}/movies/`)
      .then( (res) => {
        if (this.$store.state.movies.length === 0) {
          this.$store.state.movies = res.data
        }
        const randomIdx = _.random(res.data.length-1)
        this.movie = res.data[randomIdx]
        const numbers = _.range(1, res.data.length);
        const sampleNums = _.sampleSize(numbers, 30);
        

        for (const key in sampleNums) {
          this.movies.push(res.data[sampleNums[key]])
        }
      })
      .catch( (err) => {
        console.log(err)
      })
    },
    getRecommend: function () {
      const config = this.getToken()

      const item = {
        movies: this.user.like_movies,
      }
      // 내가 좋아하는 영화 좋아하는 사람 찾기
      axios.post(`${SERVER_URL}/movies/${this.user.id}/like/users/`,item , config)
      .then( (res) => {
        // console.log(res)
        // this.my_like_users = res.data
        const item = {
          users: res.data,
        }

        // 그 사람들이 좋아하는 영화 찾기
        axios.post(`${SERVER_URL}/accounts/info/`, item, config)
        .then( (res) => {
          // console.log(res)
          this.my_like_users_movies = res.data

          // 일반적인 추천 받기
          const item2 = {
            like_movies: this.my_like_users_movies
          }

          axios.post(`${SERVER_URL}/movies/recommend/`, item2, config)
          .then( (res) => {
            // console.log(res)
            this.favorite_movies = res.data[0]
            this.shortest_movies = res.data[1]
            this.users_movies = res.data[2]
            this.my_users_like_movies = res.data[3]
          })
          .catch( (err) => {
            console.log(err)
          })

        })
        .catch( (err) => {
          console.log(err)
        })
      })
      .catch( (err) => {
        console.log(err)
      })
    },
    getMyName: function () {
      const config = this.getToken()

      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post(`${SERVER_URL}/accounts/myprofile/`, info, config)
      .then( (res) => {
        console.log(res)
        this.user = res.data
        this.getRecommend()
      })
      .catch( (err) => {
        console.log(err)
      })
    },    
  },
  created: function () {
    this.getMovieDatas()
    this.getMyName()
    // this.getRecommend()
  },
}
</script>

<style>
  .main {
    width: 90%;
    height: 50%;
    object-fit: cover;
  }
    .banner {
        -moz-align-items: center;
        -webkit-align-items: center;
        -ms-align-items: center;
    width: 80%;
    height: 50%;    
    object-fit: cover;
        align-items: center;
        display: -moz-flex;
        display: -webkit-flex;
        display: -ms-flex;
        display: flex;
        -moz-justify-content: center;
        -webkit-justify-content: center;
        -ms-justify-content: center;
        justify-content: center;
        /* padding: 8em 4em 6em 4em; */
        /* min-height: 70vh; */
        background-position: center;
        background-size: cover;
        background-repeat: no-repeat;
        border-top: 0;
        position: relative;
        text-align: center;
        overflow: hidden;
    }

  .inner {
    text-align: center;
    position: relative;
    z-index: 2;
  }


  .more {
    background-position: center 1.35em;
    background-repeat: no-repeat;
    background-size: auto;
    border: 1px solid #fff;
    border-radius: 100%;
    color: rgba(255, 255, 255, 0.75);
    display: block;
    height: 4em;
    text-indent: 4em;
    overflow: hidden;
    white-space: nowrap;
    width: 4em;
    z-index: 2;
    margin: 0 auto 2em auto;
  }
</style>
