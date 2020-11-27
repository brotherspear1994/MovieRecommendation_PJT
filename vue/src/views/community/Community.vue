<template>
  <div>
    <!-- <h2 class="st-font" style="margin-bottom: 20px">Community</h2> -->
    <CreateCommunity @communities-updated="communitiesUpdated" style="margin-bottom: 30px"/>
    <CommunityList :communities="communities"/>
  </div>
</template>

<script>
import CommunityList from '@/components/CommunityList'
import CreateCommunity from '@/components/CreateCommunity'

import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Community',
  components: {
    CommunityList,
    CreateCommunity,
  },
  data: function () {
    return {
      communities: [],
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

      // 장고 서버에 get 요청을 보내 전체 게시글 데이터를 가져온다.
      axios.get(`${SERVER_URL}/movies/community_list_create/`, config)
        .then((res) => {
          this.communities = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    communitiesUpdated: function () {
      this.getCommunities()
      // 새로운 게시글이 추가됐음을 알리는 이벤트가 발생하면 getCommunities 함수를 실행해준다.
    } 
  },
  created: function () {
    this.getCommunities()
    // 페이지가 처음 로딩되자마자 getCommunities 함수를 실행시켜 게시글 리스트를 쭈욱 보여준다.
  },

}
</script>

<style>

</style>
