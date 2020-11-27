<template>
  <Bubble id="page-wrap">
    <span><router-link :to="{ name: 'Intro' }" class="far fa-hand-rock font-weight-bolder text-white"> Intro</router-link></span>
    <span v-if="login"><router-link :to="{ name: 'Recommend' }" class="far fa-thumbs-up font-weight-bolder text-white"> Recommend</router-link></span>
    <span v-if="login"><router-link :to="{ name: 'Community' }" class="fas fa-church font-weight-bolder text-white"> Community</router-link></span>
    <!-- <span v-if="login"><router-link :to="{ name: 'Review' }" class="fas fa-search font-weight-bolder text-white"> Review</router-link></span> -->
    <span v-if="login"><router-link :to="{ name: 'Users' }" class="fas fa-user-friends font-weight-bolder text-white"> Users</router-link></span>
    <span v-if="login"><router-link :to="{ name: 'MyProfile' }" class="fas fa-id-card-alt font-weight-bolder text-white"> MyProfile</router-link></span>
    <span v-if="login"><router-link @click.native="logout" to="#" class="fas fa-sign-out-alt font-weight-bolder text-white"> Logout</router-link></span>
    <span v-if="!login"><router-link :to="{ name: 'SignUp' }" class="fas fa-user-plus font-weight-bolder text-white"> SignUp</router-link></span>
    <span v-if="!login"><router-link :to="{ name: 'Login' }" class="fas fa-sign-in-alt font-weight-bolder text-white"> Login</router-link></span>

  </Bubble>
</template>

<script>
import { Bubble } from 'vue-burger-menu'

export default {
  name: "Menu",
  components: {
    Bubble
  },
  props: {
    login_info: Boolean
  },
  data: function () {
    return {
      login: false,
    }
  },
  methods: {
    logout: function () {
      localStorage.removeItem('jwt')
      this.login = false
      this.$router.push({ name: "Login" })
    },
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.login = true
    }
  },
  computed: {
    loginStatus: function () {
      return this.$store.state.login
    }
  },
  watch: {
    loginCheck: function () {
      if (this.$store.state.login) {
        this.login=true
      }
    }
  }
}
</script>

<style>
 .routr-color {
   color: rgb(240, 20, 20)
 }
</style>
