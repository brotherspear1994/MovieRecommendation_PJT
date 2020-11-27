<template>
  <div class="container">
    <div class="container" style="margin-bottom:30px">
      <div class="row">
          <div class="well profile">
                <div class="col-sm-12">
                    <div class="col-xs-12 col-sm-8 center" style="margin-bottom:20px">
                        <h2 class="title-font" style="margin-bottom: 30px">{{ user.username }}님의 Profile</h2>
                        <p class="content-font" style="font-size: 20px"><strong>Email: </strong> {{ user.email }} </p>
                        <p class="content-font" style="font-size: 20px"><strong>Info: </strong>
                            <span class="tags" style="margin-right:5px">{{user.age}}</span> 
                            <span class="tags" style="margin-right:5px">{{user.sex}}</span>
                        </p>
                        <p v-if="isFollowing" class="st-font">{{ user.username }}님을 팔로우 중 입니다.</p>
                    </div>
                    <br>             
                    <div class="col-xs-12 col-sm-4 text-center">
                        <figure>
                            <img src="@/assets/미니언즈.jpg" alt="" class="img-circle img-responsive">
                        </figure>
                    </div>
                </div>            
                <div class="col-xs-12 divider text-center">
                    <div class="col-xs-12 col-sm-4 emphasis">
                        <h2><strong v-if="user.followers">{{followersLength}}</strong></h2>                    
                        <p><small>Followers</small></p>
                    </div>
                    <div class="col-xs-12 col-sm-4 emphasis">
                        <h2><strong>{{followingsLength}}</strong></h2>                    
                        <p><small>Following</small></p>
                    </div>
                    <div class="col-xs-12 col-sm-4 emphasis">
                        <h2><strong v-if="user.followings">{{user.like_movies.length}}</strong></h2>                    
                        <p><small>'좋아요'한 영화 수</small></p>
                    </div>
                </div>
                <button v-if="isFollowing" @click="follow" class="btn btn-secondary btn-block"><span class="fa fa-plus-circle"></span> UnFollow </button>
                <button v-else @click="follow" class="btn btn-primary btn-block"><span class="fa fa-plus-circle"></span> Follow </button>
          </div>                 
      </div>
    </div>
    <h2 class="title-font">{{ user.username }}님이 좋아요 한 영화</h2>    
    <ul v-if="usersMovies">
      <MovieCard 
        :movies="usersMovies"
      />
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"

import MovieCard from "@/components/MovieCard"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "Profile",
  props: {
    user_pk: {
      type: Number,
    },
    username: {
      type: String,
    },
  },
  components: {
    MovieCard,
  },
  data: function () {
    return {
      user: [],
      me: [],
      following: '',
      usersMovies: [],
    }
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
    getMyName: function () {
      const config = this.getToken()

      const hash = localStorage.getItem('jwt')
      // console.log(VueJwtDecode.decode(hash))
      const info = VueJwtDecode.decode(hash)
      axios.post(`${SERVER_URL}/accounts/myprofile/`, info, config)
      .then( (res) => {
        // console.log(res.data)
        this.me = res.data
        if (this.me.followings.includes(this.user.id)) {
          this.following = true
        } else {
          this.following = false
        }
        // console.log(this.me.followings)
      })
      .catch( (err) => {
        console.log(err)
      })
    },
    getUserInfoSub: function () {
      const config = this.getToken()
      const user_pk = this.$route.params.user_pk
      const username = this.$route.params.username
      const userItem = {
        user_pk: user_pk,
        username: username,
      }
      axios.post(`${SERVER_URL}/accounts/${username}/`, userItem, config)
      .then( (res) => {
        // console.log(res.data)
        // console.log(res)
        this.user = res.data
      })
      .catch( (err) => {
        console.log(err)
      })
    },
    getUserInfo: function () {
      const config = this.getToken()
      const user_pk = this.$route.params.user_pk
      const username = this.$route.params.username
      const userItem = {
        user_pk: user_pk,
        username: username,
      }
      axios.post(`${SERVER_URL}/accounts/${username}/`, userItem, config)
      .then( (res) => {
        // console.log(res.data)
        // console.log(res)
        this.user = res.data
        const item = this.user.like_movies

        axios.post(`${SERVER_URL}/movies/${this.user.id}/like/`, item, config)
        .then( (res) => {
          // console.log(res)
          this.usersMovies = res.data
        })
        .catch( (err) => {
          console.log(err)
        })

      })
      .catch( (err) => {
        console.log(err)
      })
    },
    follow: function () {
      const config = this.getToken()
      const item = {
        myId: this.me.id,
        userId: this.user.id,
      }

      axios.post(`${SERVER_URL}/accounts/follow/${this.me.id}/${this.user.id}/`, item, config)
      .then( () => {
        // console.log(res)
        
        // console.log(this.me)
        this.getMyName()
        this.getUserInfoSub()
      })
      .catch( (err) => {
        console.log(err)
      })
    },
  },
  computed: {
    isFollowing: function () {
      return this.following
    },
    followingsLength: function () {
      if (this.user.followings) {
        return this.user.followings.length
      } else {
        return 0
      }
    },
    followersLength: function () {
      if (this.user.followers) {
        return this.user.followers.length
      } else {
        return 0
      }
    },
  },
  created: function () {
    this.getUserInfo()
    this.getMyName()
  },
}
</script>

<style>
@import url(http://fonts.googleapis.com/css?family=Lato:400,700);
.center {
    position: relative;
    top: 50px;
}

.profile 
{
min-height: 355px;
display: inline-block;
}
.divider 
{
border-top:1px solid rgba(0,0,0,0.1);
}
.emphasis 
{
border-top: 4px solid transparent;
}
.emphasis:hover 
{
border-top: 4px solid #1abc9c;
}
.emphasis h2
{
margin-bottom:0;
}
span.tags 
{
background: #404242;
border-radius: 2px;
color: #f5f5f5;
font-weight: bold;
padding: 4px 6px;
}

</style>
