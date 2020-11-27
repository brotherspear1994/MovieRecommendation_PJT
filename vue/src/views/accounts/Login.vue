<template>
  <div>
    <section class="page-section" id="contact">
        <div class="container">

            <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Login</h2>

            <div class="row">
                <div class="col-lg-8 mx-auto">
                    
                  <div class="control-group">
                      <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                          <label for="username">Username</label>
                          <input style="font-size: 30px" v-model.trim="credentials.username" class="form-control" id="username" type="text" placeholder="Username" required="required" data-validation-required-message="Please enter your username." />
                          <p class="help-block text-danger"></p>
                      </div>
                  </div>
                  <div class="control-group">
                      <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                          <label>password</label>
                          <input style="font-size: 30px" @keypress.enter="login" v-model.trim="credentials.password" class="form-control" id="password" type="password" placeholder="Password" required="required" data-validation-required-message="Please enter your password." />
                          <p class="help-block text-danger"></p>
                      </div>
                  </div>
                  <br />
                  <div id="success"></div>
                  <div class="text-white st-font form-group"><button @click="login" class="btn btn-secondary btn-xl" id="Login" type="submit">Login</button></div>
                  <h3 class="st-font">회원정보가 없다면 아래 회원가입을 눌러주세요.</h3>
                  <div class="text-white st-font form-group"><button @click="moveToSignUp" class="btn btn-secondary btn-xl" id="Signup" type="submit">Signup</button></div>
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
  name: "Login",
  data: function () {
    return {
      loginStatus: false,
      credentials: {
        username: '',
        password: '',
      },
    }
  },
  methods: {
    login: function () {
      axios.post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
      .then( (res) => {
        // console.log(res)
        localStorage.setItem('jwt', res.data.token)
        // this.$emit('login')
        // this.loginStatus = true
        // this.$store.dispatch("loginChange", this.loginStatus)
        this.$router.push({ name: "Recommend" })
        location.reload()
      })
      .catch( (err) => {
        alert("올바른 아이디와 비밀번호를 입력해주세요.")
        console.log(err)
      })
    },
    moveToSignUp: function () {
      this.$router.push({ name: 'SignUp' })
    }
  }
}
</script>

<style>

</style>
