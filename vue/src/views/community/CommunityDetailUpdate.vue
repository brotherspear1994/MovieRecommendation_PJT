<template>
  <div>
    <section class="page-section" id="contact">
        <div class="container">
            <!-- Contact Section Heading-->
            <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Detail Update</h2>
            <!-- Contact Section Form-->
            <div class="row">
                <div class="col-lg-8 mx-auto">
                    <!-- To configure the contact form email address, go to mail/contact_me.php and update the email address in the PHP file on line 19.-->
                  <div class="control-group">
                      <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                          <label>Title</label>
                          <input style="font-size: 30px" v-model.trim="community.title" class="form-control" id="title" type="text" placeholder="Title" required="required" data-validation-required-message="Please enter your title." />
                          <p class="help-block text-danger"></p>
                      </div>
                  </div>
                  <div class="control-group">
                      <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                          <label>Content</label>
                          <textarea style="font-size: 30px" v-model.trim="community.content" class="form-control" id="content" rows="5" placeholder="Content" required="required" data-validation-required-message="Please enter a message."></textarea>
                          <p class="help-block text-danger"></p>
                      </div>
                  </div>
                  <br />
                  <div id="success"></div>
                  <div class="text-white st-font form-group"><button @click="communityDetailUpdate(community)" class="btn btn-secondary btn-xl" id="sendMessageButton" type="submit">Update</button></div>
                </div>
            </div>
        </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
    name: 'CommunityDetailUpdate',
    props: {
        community_pk: Number,
    },
    data: function () {
        return {
            community: [],
            // community_title: '',
            // community_content: '',
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
        getCommunity: function () {
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
        communityDetailUpdate: function (community) {
        const config = this.getToken()
        
        const communityItem = {
            title: community.title,
            content: community.content
        }

        axios.put(`${SERVER_URL}/movies/community/${community.id}/`, communityItem, config)
            .then((res) => {
                if (res.data.message) {
                    alert("본인이 작성한 글만 수정 가능합니다!")
                }
                else {
                    this.$router.push({ name: 'CommunityDetail', params: { community_pk: `${community.id}` }})
                }
            })
            .catch((err) => {
                console.log(err)
            })
        },        
    },
    created: function () {
        this.getCommunity()
    }    
}
</script>

<style>

</style>