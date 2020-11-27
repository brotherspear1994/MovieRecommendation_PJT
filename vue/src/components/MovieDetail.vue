<template>
  <div class="container">
    <v-hover style="margin-bottom:10px">
      <template v-slot:default="{ hover }">
        <v-card>
          <v-img style="overflow-y: hidden; height:300px;" :src="`https://image.tmdb.org/t/p/w300${movie.poster_path}`"></v-img>
          <v-fade-transition>
            <v-overlay
              v-if="hover"
              absolute
              color="#036358"
            >
              <v-btn class="st-font" style="margin-bottom:10px" @click="movieDetail()">See more info</v-btn>
              <div>
                <span v-for="(i, idx) in rating" :key="idx">
                  <i style="color:yellow;" class="fas fa-star"></i>
                </span>
              </div>
            </v-overlay>
          </v-fade-transition>
          <!-- <p class="content-font" style="font-weight: bold;">{{ movie.title }}</p> -->
        </v-card>  
      </template>
    </v-hover>
    <div class="container">
      <b-modal
        hide-footer
        v-model="show"
        id="movie-modal"
        size="lg"
        :title="movie.title"
        :header-bg-variant="headerBgVariant"
        :header-text-variant="headerTextVariant"
        :body-bg-variant="bodyBgVariant"
        :body-text-variant="bodyTextVariant"
        :footer-bg-variant="footerBgVariant"
        :footer-text-variant="footerTextVariant"
      >
        <img :src="`https://image.tmdb.org/t/p/w300${movie.poster_path}`" id="myImg">

        <i id="heart" v-if="isLiking" @click="like" style="color:crimson; font-size:60px; text-align:center; margin-top:30px;" class="fas fa-heart"></i>
        <i id="heart" v-else @click="like" style="font-size:60px; text-align:center; margin-top:30px;" class="far fa-heart"></i>
        <p class="st-font" style="text-align:center; margin-top:5px">좋아요 {{ numLike }}개</p>

        <hr>

        <h5 style="margin-bottom:10px" class="title-font">영화 제목 : {{ movie.title }}</h5>
        <h5 style="margin-bottom:10px" class="content-font">평점 : {{ movie.vote_average }}점</h5>
        <h5 style="margin-bottom:10px" class="content-font">상영 시간 : {{ movie.runtime }}분</h5>
        <h5 style="margin-bottom:10px" class="content-font">개봉 일자 : {{ movie.release_date }}</h5>
        <h5 style="margin-bottom:10px" class="content-font">좋아요 {{ numLike }}개</h5>

        <hr>
        <span v-if="movie.overview" class="st-font">{{ movie.overview }}</span>
        <span v-else class="st-font">해당 영화의 overview는 비어있습니다.</span>
        <hr>
        <MovieReview 
          :movie="movie"
        />
        <div class="text-white st-font form-group"><button @click="close" class="btn btn-secondary btn-xl" id="sendMessageButton" type="submit">리뷰 창 닫기</button></div>
      </b-modal>
    </div>
  </div>
</template>

<script>
import MovieReview from '@/components/MovieReview'

import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "MovieDetail",
  components: {
    MovieReview,
  },
  data: function () {
    return {
      show: false,
      variants: ["light", "dark"],
      headerBgVariant: "dark",
      headerTextVariant: "white",
      bodyBgVariant: "dark",
      bodyTextVariant: "white",
      footerBgVariant: "danger",
      footerTextVariant: "dark",
      reviews: [],
      me: [],
      liking: '',
      numLike: '',
      rating: Number(this.movie.vote_average),
    }
  },
  props: {
    movie: {
      type: Object,
    }
  },
  methods: {
    movieDetail: function () {
      this.show = true
    },
    ratingToInt: function () {
      this.rating = Math.ceil(this.rating / 2)
    },
    close: function () {
      this.show = false
    },
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
        // console.log(this.me)
        if (this.me.like_movies.includes(this.movie.id)) {
          this.liking = true
        } else {
          this.liking = false
        }
      })
      .catch( (err) => {
        console.log(err)
      })
    },
    like: function () {
      const config = this.getToken()
      const item = {
        myId: this.me.id,
        movieId: this.movie.id,
      }

      axios.post(`${SERVER_URL}/movies/${this.me.id}/${this.movie.title}/like/`, item, config)
      .then( () => {
        this.getMyName()
        this.check()
        // console.log(res)
      })
    },
    number: function () {
      this.numLike = this.movie.like_users.length
      // console.log(this.rating)
    },
    check: function () {
      if (this.liking) {
        this.numLike -= 1
      } else {
        this.numLike += 1
      }
    }
  },
  computed: {
    isLiking: function () {
      return this.liking
    },
  },
  created: function () {
    this.getMyName()
    this.number()
    this.ratingToInt()
  },
}
</script>


<style>
#myImg {
  display: block;
  margin: 0px auto;
}
#heart {
  display: block;
  margin: 0px auto;
  cursor: pointer;
  -webkit-transition-duration: 0.4s;
  transition-duration: 0.4s;
}
#heart:hover {
  color: crimson;
}
.w3-myfont {
  font-family: 'Luminari', fantasy;
}
.w2-myfont {
  font-family: 'Avantgarde', 'TeX Gyre Adventor', 'URW Gothic L', sans-serif;
}

#main {
padding: 4em 0 2em 0;
}

@media screen and (max-width: 736px) {

#main {
padding: 3em 0 1em 0;
}

}

#main .inner {
width: 90%;
max-width: 80em;
margin: 0 auto;
}

@media screen and (max-width: 480px) {

#main .inner {
width: 95%;
}
}
.thumbnails {
display: -moz-flex;
display: -webkit-flex;
display: -ms-flex;
display: flex;
-moz-align-items: stretch;
-webkit-align-items: stretch;
-ms-align-items: stretch;
align-items: stretch;
-moz-justify-content: center;
-webkit-justify-content: center;
-ms-justify-content: center;
justify-content: center;
-moz-flex-wrap: wrap;
-webkit-flex-wrap: wrap;
-ms-flex-wrap: wrap;
flex-wrap: wrap;
}

.thumbnails .box {
margin: 0 1em 2em 1em;
width: 30%;
}

@media screen and (max-width: 1280px) {

.thumbnails .box {
width: 45%;
}

}

@media screen and (max-width: 736px) {

.thumbnails .box {
width: 100%;
}

}
</style>
