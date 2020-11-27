<template>
  <div>
    <section class="page-section" id="contact">
        <div class="container">
            <!-- Contact Section Heading-->
            <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Community</h2>
            <!-- Contact Section Form-->
            <div class="row">
                <div class="col-lg-8 mx-auto">
                    <!-- To configure the contact form email address, go to mail/contact_me.php and update the email address in the PHP file on line 19.-->
                  <div class="control-group">
                      <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                          <label>Title</label>
                          <input style="font-size: 30px" v-model.trim="title" class="form-control" id="title" type="text" placeholder="Title" required="required" data-validation-required-message="Please enter your title." />
                          <p class="help-block text-danger"></p>
                      </div>
                  </div>
                  <div class="control-group">
                      <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                          <label>Content</label>
                          <textarea style="font-size: 30px" v-model.trim="content" class="form-control" id="content" rows="5" placeholder="Content" required="required" data-validation-required-message="Please enter a message."></textarea>
                          <p class="help-block text-danger"></p>
                      </div>
                  </div>
                  <br />
                  <div id="success"></div>
                  <div class="text-white st-font form-group"><button @click="createCommunity" class="btn btn-secondary btn-xl" id="sendMessageButton" type="submit">Add</button></div>
                </div>
            </div>
        </div>
    </section>
  </div>
</template>

<script>
// community 게시판 게시글 작성을 위한 컴퍼넌트 페이지입니다.
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CreateCommunity',
  data: function () {
    return {
      title: '',
      content: '',
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
    // createCommunity 함수가 실행되면 입력된 제목과 콘텐츠 데이터를 params 형태로 만든뒤
    createCommunity: function () {
      const config = this.getToken()

      const communityItem = {
        title: this.title,
        content: this.content,
      }
      if (communityItem.title) {
        // axios post 요청을 장고에 데이터와 함께 보내줍니다.
        axios.post(`${SERVER_URL}/movies/community_list_create/`, communityItem, config)
          .then(() => {
            // console.log(res)
            // this.$router.push({ name: 'Community' })
            // 위의 router 요청은 게시글 작성직후 바로 해당 컴퍼넌트로 이동시켜 작성된 게시물을 바로 보여주게끔 해주는 도구이나,
            // 우리는 현재 community 페이지 내에서 작성과 글의 제목을 보는것을 모두 가능하게 하고 싶어 위 처럼 해줬을시 
            // Uncaught (in promise) NavigationDuplicated: Avoided redundant navigation to current location 이라는 에러가 발생합니다.
            // 즉 현재있는 위치에서 동일한 위치로 router 요청을 보내니 불필요한 요청이라 알려주는 것입니다.
            this.$emit('communities-updated')
            // 때문에 emit을 사용해 글이 작성됐음을 알려주는 이벤트를 보내고
            this.title = "" // 사용자경험 향상을 위해 작성한 제목과 내용은 초기화.
            this.content = ""
          })
          .catch((err) => {
            console.log(err)
          })
      } 
    }
  },
}
</script>

<style>

</style>
