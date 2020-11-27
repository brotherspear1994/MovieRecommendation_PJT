<template>
  <div>
  <div class="container">
    <h2 class="st-font" style="margin-bottom:30px">제목을 눌러 상세페이지로, 유저를 눌러 프로필로 넘어가보세요</h2>
    <div class="row">
      <div class="col-lg-8 col-md-10 mx-auto">
        <div class="post-preview" style="cursor:pointer;" v-for="(community, idx) in communities" :key="idx">
            <h3 class="title-font" @click="DetailCommunity(community)">{{community.id}}번 글</h3>
            <h2 class="title-font" @click="DetailCommunity(community)">
              {{community.title}}
            </h2>
            <h4 class="content-font">
              {{community.content}}
            </h4>
          <p class="st-font" @click="moveToProfile(community.user, community.userName)">Written by
              {{community.userName}}
          </p>
        <hr>
        </div>
      </div>
    </div>
  </div>

  </div>
</template>


<script>


export default {
  name: 'CommunityList',
  props: {
    // Community에서 v-for을 이용해 보내준 게시글 한개의 데이터를 props를 통해 받고 보여준다.
    communities: [Array, Object]
  },
  methods: {
    DetailCommunity: function (community) {
      // console.log(community)
      // this.$store.dispatch('createDetailCommunity', community)
      this.$router.push({ name: 'CommunityDetail', params: { community_pk: `${community.id}` }})
    },
    moveToProfile: function (user, username) {
      // console.log(user)
      this.$router.push({ name: "Profile", params: { user_pk: `${user}`, username: `${username}` }})
    },    
  }

}
</script>

<style>

</style>
