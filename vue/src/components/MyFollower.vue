<template>
  <div>
    <h4>{{ myFollower.username }}</h4><span><button @click="moveToProfile(myFollower)">Go to profile</button></span>
  </div>
</template>

<script>
import axios from "axios"
const SERVER_URL = process.env.VUE_APP_SERVER_URL


export default {
  name: "MyFollower",
  props: {
    follow: {
      type: Number,
    },
  },
  data: function () {
    return {
      users: [],
      myFollower: [],
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
    getUsers: function () {
      const config = this.getToken()

      axios.get(`${SERVER_URL}/accounts/users`, config)
      .then( (res) => {
        this.users = res.data
        const idx = this.users.findIndex((item) => {
          return item.id === this.follow
        })
        this.myFollower = this.users[idx]
      })
      .catch( (err) => {
        console.log(err)
      })
    },
    moveToProfile: function (user) {
      this.$router.push({ name: "Profile", params: { user_pk: `${user.id}`, username: `${user.username}` }})
    },
  },
  created: function () {
    this.getUsers()
  },
}
</script>

<style>

</style>
