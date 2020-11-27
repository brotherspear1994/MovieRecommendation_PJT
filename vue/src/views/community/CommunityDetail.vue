<template>
  <div>
    <div class="container">
      <div>
        <h2 class="title-font">{{community.userName}}님의 게시글</h2>
        <hr>
        <div class="st-font" style="margin-bottom:30px">
          <span @click="moveToProfile(community)" style="cursor:pointer;">작성자: {{ community.userName }} | </span>  
          <span>글 생성시간: {{ community.created_at }} | </span>
          <span>글 수정시간: {{ community.updated_at }}</span>  
        </div>
        <div>
          <p class="title-font" style="font-size: 40px">제목: {{ community.title }}</p>
          <p class="content-font" style="font-size: 50px">내용: {{ community.content }}</p>
        </div>
      </div>
      <button @click="moveToDetailUpdate(community)" type="button" class="st-font btn btn-secondary text-white" style="margin-right:10px">수정</button>
      <button @click="deleteCommunity(community)" type="button" class="st-font btn btn-secondary text-white" style="margin-right:10px">삭제</button>
    </div>
    <br>
    <section class="page-section" id="contact">
        <div class="container">
            <div class="row">
                <div class="col-lg-8 mx-auto">
                    <!-- To configure the contact form email address, go to mail/contact_me.php and update the email address in the PHP file on line 19.-->
                  <div class="control-group">
                      <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                          <label>댓글 작성</label>
                          <textarea v-model.trim="comment_content" style="font-size: 30px" class="form-control" id="content" rows="5" placeholder="Comment" required="required" data-validation-required-message="Please writer a comment."></textarea>
                          <p class="help-block text-danger"></p>
                      </div>
                  </div>
                  <div id="success"></div>
                  <div class="text-white st-font form-group" style="font-weight"><button @click="createComment" class="btn btn-secondary btn-xl" id="sendMessageButton" type="submit">댓글 작성</button></div>
                </div>
            </div>
        </div>
    </section>
    <br>
    <div class="container" v-for="(comment, idx) in commentsList" :key="idx">
        <div class="row">
            <div class="col-8">
                <div class="card card-white post">
                    <div class="post-heading">
                        <div class="float-left image">
                            <img style="margin-right:10px" src="@/assets/가오나시.png" class="img-circle avatar" alt="user profile image">
                        </div>
                        <div class="float-left meta">
                            <div class="title h5 st-font">
                                <b style="cursor:pointer;" @click="moveToProfile(comment.user, comment.userName)">{{comment.userName}}</b>
                                님이 댓글을 작성하셨습니다.
                            </div>
                            <h6 class="title-font text-muted time">{{comment.created_at}}</h6>
                        </div>
                    </div> 
                    <div style="font-size:30px" class="content-font post-description"> 
                        <p>{{comment.content}}</p>
                    </div>
                <button class="st-font button1" style="cursor:pointer;" @click="deleteComment(community, comment)">삭제</button>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"
const SERVER_URL = process.env.VUE_APP_SERVER_URL


export default {
  name: 'CommunityDetail',
  props: {
    community_pk: Number,
  },
  data: function () {
    return {
      community: [],
      comment_content: '',
      comments: [],
      user: [],
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
    getCommunities: function () {
      const config = this.getToken()

      const community_pk = this.$route.params.community_pk
      // 장고 서버에 get 요청을 보내 전체 게시글 데이터를 가져온다.
      axios.get(`${SERVER_URL}/movies/detail/${community_pk}/`, config)
        .then((res) => {
          // console.log(res)
          this.community = res.data
        })
        .catch((err) => {
          console.log(err)
        })    
    },
    getMyName: function () {
      const config = this.getToken()

      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post(`${SERVER_URL}/accounts/myprofile/`, info, config)
      .then( (res) => {
        this.user = res.data
        // console.log(this.user)
      })
      .catch( (err) => {
        console.log(err)
      })
    },
    getComments: function () {
      const config = this.getToken()

      const community_pk = this.$route.params.community_pk

      axios.get(`${SERVER_URL}/movies/comments/${community_pk}`, config)
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
      }
      if (commentItem.content) {
        axios.post(`${SERVER_URL}/movies/${this.community.id}/comment/`, commentItem, config)
          .then( () => {
            // console.log(res)
          this.getComments()
          this.comment_content = ''
          })
        }
    },
    deleteCommunity: function (community) {
      const config = this.getToken()

      axios.delete(`${SERVER_URL}/movies/community/${community.id}/`, config)
        .then((res) => {
          // console.log(res)
          if (res.data.message) {
            alert("본인이 작성한 글만 삭제 가능합니다!")
          }
          else {
            this.$router.push({ name: 'Community' })
          }
        })
    },
    deleteComment: function (community, comment) {
      const config = this.getToken()
      axios.delete(`${SERVER_URL}/movies/comment/${community.id}/${comment.id}/`, config)
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
    moveToDetailUpdate: function (community) {
      // console.log(this.user)
      if (this.user.username === community.userName) {
        this.$router.push({ name: 'CommunityDetailUpdate', params: { community_pk: `${community.id}` }})
      } else {
        alert("본인이 작성한 글만 수정 가능합니다!")
      }
      
    },
    moveToProfile: function (community) {
      // console.log(community.userName)
      this.$router.push({ name: "Profile", params: { user_pk: `${community.user}`, username: `${community.userName}` }})
    },   
  },
  computed: {
    commentsList: function () {
      return this.comments
    }
  },
  created: function () {
    this.getCommunities()
    this.getComments()
    this.getMyName()
  }
}
</script>

<style>
.button1 {
  background-color: white;
  color: black;
  border: 2px solid #050505;
}
.button5 {background-color: #555555;}
</style>
