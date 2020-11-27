<template>
  <div>
    <div class="row">
      <div class="col-lg-8 col-md-10 mx-auto">
        <div class="post-preview" style="cursor:pointer;">
            <h2 class="title-font" @click="detailReview(review)">
              제목 | {{ review.title }}
            </h2>
            <h4 class="content-font" style="margin-bottom:30px">
              내용 | {{review.content}}
            </h4>
            <button @click="updateReview(review)" type="button" class="st-font btn btn-secondary text-white" style="margin-right:10px">수정</button>
            <button @click="deleteReview(review)" type="button" class="st-font btn btn-secondary text-white" style="margin-right:10px">삭제</button>
            <hr>
        </div>
      </div>
    </div>
    <div class="container">
      <b-modal
        hide-footer
        v-model="show"
        id="review-modal"
        size="lg"
        :title="review.title"
        :header-bg-variant="headerBgVariant"
        :header-text-variant="headerTextVariant"
        :body-bg-variant="bodyBgVariant"
        :body-text-variant="bodyTextVariant"
        :footer-bg-variant="footerBgVariant"
        :footer-text-variant="footerTextVariant"
      >
        <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" id="myImg">
        <hr>
        <h4 class="title-font">리뷰 제목 | {{ review.title }}</h4>
        <h5 class="content-font">작성자 | {{ review.userName }}</h5>
        <h5 class="content-font">리뷰 내용 | {{ review.content }}</h5>
        <h5 class="st-font">남긴 평점 | {{ review.rank }}점</h5>
        <hr>
        <!-- 댓글란 -->
        <section class="page-section" id="contact">
          <div class="container">
            <h2 class="page-section-heading text-center text-uppercase text-white mb-0 title-font">댓글 작성</h2>
            <div class="row">
              <div class="col-lg-8 mx-auto">
                <div class="control-group">
                  <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                    <label for="comment">댓글: </label>
                    <input v-model.trim="comment_content" class="form-control" id="comment" type="text" placeholder="Comment" required="required" data-validation-required-message="Please enter your comment." />
                    <p class="help-block text-danger"></p>
                  </div>
                </div>

                <label style="margin-right: 15px" class="st-font" for="rank">내가 생각하는 영화 평점</label>
                <div class="select-wrapper" style="margin-right: 15px">            
                  <select name="rate" id="rate" v-model="myMovieRate" class="content-font">
                    <option class="content-font" style="color:black;" :value="rate" v-for="(rate, idx) in this.$store.state.reviewRate" :key="idx">{{ rate }}</option>
                  </select>
                </div>

                <br />
                <div id="success"></div>
                <div class="text-white st-font form-group"><button @click="createComment" class="btn btn-secondary btn-xl" id="createComment" type="submit">댓글작성</button></div>

              </div>

            </div>
          </div>
        </section>
        <br>
        <div>
          <h5 class="title-font">댓글 목록</h5>
          <div style="display:flex;" class="container" v-for="(comment, idx) in commentsList" :key="idx">
            <div class="row">
                <div class="col-8 mx-auto" id="reviewComment">
                    <div class="card card-white post">
                        <div class="post-heading">
                            <div class="float-left image">
                                <img style="margin-right:10px" src="@/assets/귀요미2.jpg" class="img-circle avatar" alt="user profile image">
                            </div>
                            <div class="float-left meta">
                                <div class="title h5 st-font">
                                    <b style="cursor:pointer;" @click="moveToProfile2(comment)">{{comment.userName}}</b>
                                    님이 댓글을 작성하셨습니다.
                                </div>
                                <h6 class="title-font text-muted time">{{comment.created_at}}</h6>
                            </div>
                        </div> 
                        <div style="font-size:30px" class="content-font post-description"> 
                            <p>{{comment.content}}</p>
                            <p>나의 영화 평점 : {{ comment.rank }}</p>
                        </div>
                    <button class="st-font button1" style="cursor:pointer;" @click="deleteComment(review, comment)">삭제</button>
                    </div>
                </div>
            </div>
          </div>
          <!-- <ul v-for="(comment, idx) in commentsList" :key="idx">
            <div>
              <li>{{ comment.userName }}: {{ comment.content }} - 댓글 생성 시각: {{ comment.created_at }}</li>
              <p>영화 평점 : {{ comment.rank }}</p>
              <button @click="deleteComment(review, comment)">X</button>
            </div>
          </ul> -->
        </div>
        
        <hr>	
        <div class="text-white st-font form-group"><button @click="close" class="btn btn-secondary btn-xl" id="sendMessageButton" type="submit">창 닫기</button></div>
      </b-modal>
    </div>


    <div class="container">
      <b-modal
        hide-footer
        v-model="show2"
        id="review-modal"
        size="lg"
        :title="review.title"
        :header-bg-variant="headerBgVariant"
        :header-text-variant="headerTextVariant"
        :body-bg-variant="bodyBgVariant"
        :body-text-variant="bodyTextVariant"
        :footer-bg-variant="footerBgVariant"
        :footer-text-variant="footerTextVariant"
      >
        <hr>
        <section class="page-section" id="contact">
          <div class="container">
              <!-- Contact Section Heading-->
              <h2 class="title-font page-section-heading text-center text-uppercase text-white mb-0">리뷰 수정</h2>
              <!-- Contact Section Form-->
              <div class="row">
                  <div class="col-lg-8 mx-auto">
                      <!-- To configure the contact form email address, go to mail/contact_me.php and update the email address in the PHP file on line 19.-->
                    <div class="control-group">
                        <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                            <label>리뷰 제목:</label>
                            <input v-model.trim="title" class="form-control" id="reviewTitle" type="text" :placeholder="review.title" required="required" data-validation-required-message="Please enter your review title." />
                            <p class="help-block text-danger"></p>
                        </div>
                    </div>

                    <div class="control-group">
                        <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                            <label>영화 제목: {{ movie.title }}</label>
                            <!-- <p class="help-block text-danger"></p> -->
                        </div>
                    </div>

                    <label style="margin-right: 15px" class="st-font" for="rank">내가 생각하는 영화 평점</label>
                    <div class="select-wrapper" style="margin-right: 15px">            
                      <select name="rate" id="rate" v-model="myMovieRate2" class="content-font">
                        <option class="content-font" style="color:black" :value="rate" v-for="(rate, idx) in this.$store.state.reviewRate" :key="idx">{{ rate }}</option>
                      </select>
                    </div>

                    <div class="control-group">
                        <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                            <label>리뷰 내용</label>
                            <textarea v-model.trim="content" class="form-control" id="content" rows="5" :placeholder="review.content" required="required" data-validation-required-message="Please enter a content."></textarea>
                            <p class="help-block text-danger"></p>
                        </div>
                    </div>
                    <br />
                    <div id="success"></div>
                    <div class="text-white st-font form-group"><button @click="update(review)" class="btn btn-secondary btn-xl" id="sendMessageButton" type="submit">수정 !</button></div>
                  </div>
              </div>
          </div>
        </section>
        <div class="text-white st-font form-group"><button @click="close2" class="btn btn-secondary btn-xl" id="sendMessageButton" type="submit">창 닫기</button></div>
      </b-modal>
    </div>


  </div>
</template>

<script>
import axios from 'axios'
// import VueJwtDecode from "vue-jwt-decode"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "MovieReviewDetail",
  props: {
    review: {
      type: Object
    },
    movie: {
      type: Object
    },
  },
  data: function () {
    return {
      show: false,
      show2: false,
      variants: ["light", "dark"],
      headerBgVariant: "dark",
      headerTextVariant: "white",
      bodyBgVariant: "dark",
      bodyTextVariant: "white",
      footerBgVariant: "danger",
      footerTextVariant: "dark",
      comment_content: '',
      comments: [],
      myMovieRate: 0,
      title: '',
      content: '',
      myMovieRate2: 0,
    }
  },
  methods: {
    detailReview: function () {
      this.show = true
    },
    updateReview: function () {
      this.show2 = true
    },
    close: function () {
      this.show = false
    },
    close2: function () {
      this.show2 = false
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
    deleteReview: function (review) {
      const config = this.getToken()

      axios.delete(`${SERVER_URL}/movies/review/${review.id}/`, config)
        .then((res) => {
          // console.log(res)
          if (res.data.message) {
            alert("본인이 작성한 글만 삭제 가능합니다!")
          }
          else {
            this.$emit('deleteReview')
          }
        })
    },
    getComments: function () {
      const config = this.getToken()

      axios.get(`${SERVER_URL}/movies/review_comments/${this.review.id}`, config)
        .then((res) => {
          this.comments = res.data
          // console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    createComment: function () {
      const config = this.getToken()
      
      const commentItem = {
        content: this.comment_content,
        rank: this.myMovieRate,
      }
      if (commentItem.content) {
        axios.post(`${SERVER_URL}/movies/${this.review.id}/review_comment/`, commentItem, config)
          .then( () => {
            // console.log(res)
          this.getComments()
          this.comment_content = ''
          })
        }
    },
    deleteComment: function (review, comment) {
      const config = this.getToken()
      axios.delete(`${SERVER_URL}/movies/review_comment/${review.id}/${comment.id}/`, config)
        .then((res) => {
          // console.log(res)
          if (res.data.message) {
            alert("본인이 작성한 댓글만 삭제 가능합니다!")
          }
          else {
            this.getComments()
          }
        })
    },
    moveToProfile: function (review) {
      // console.log(review.userName)
      this.$router.push({ name: "Profile", params: { user_pk: `${review.user}`, username: `${review.userName}` }})
    },
    moveToProfile2: function (comment) {
      // console.log(review.userName)
      this.$router.push({ name: "Profile", params: { user_pk: `${comment.user}`, username: `${comment.userName}` }})
    },
    update: function (review) {
      const config = this.getToken()

      const reviewItem = {
        title: this.title,
        content: this.content,
        rank: this.myMovieRate2,
        movie: review.movie,
      }

      axios.put(`${SERVER_URL}/movies/review/${review.id}/`, reviewItem, config)
      .then( (res) => {
        if (res.data.message) {
          alert("본인이 작성한 글만 수정 가능합니다!")
        }
        else {
          this.close2()
          this.$emit("reviews-updated")
        }
      })
      .catch( (err) => {
        console.log(err)
      })
    }
  },
  computed: {
    commentsList: function () {
      return this.comments
    },
  },
  created: function () {
    // this.getMyName()
    this.getComments()
  }
  
}
</script>

<style>
#reviewComment {
  color: darkslategray !important
}
#myImg {
  display: block;
  margin: 0px auto;
}
#reviewBtn {
  margin-left: 60px;
  padding: 1px;
  color: white;
  border: 2px solid darkkhaki;
}
</style>
