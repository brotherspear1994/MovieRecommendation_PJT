<template>
  <div>
    <section class="page-section" id="contact">
        <div class="container">

            <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Signup</h2>

            <div class="row">
                <div class="col-lg-8 mx-auto">
                    
                  <div class="control-group">
                      <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                          <label for="username">Username</label>
                          <input style="font-size: 30px" v-model.trim="credentials.username" class="form-control" id="username" type="text" placeholder="Username" required="required" data-validation-required-message="Please enter your username." />
                          <h6>Username에는 알파벳만 가능합니다.</h6>
                          <p class="help-block text-danger"></p>
                      </div>
                  </div>

                  <label style="margin-right: 15px" class="st-font" for="sex">Age </label>
                  <div class="select-wrapper" style="margin-right: 15px">            
                    <select style="font-size: 20px" name="age" id="age" v-model="credentials.age" class="st-font">
                      <option :value="age" v-for="(age, idx) in this.$store.state.ages" :key="idx">{{ age }}</option>
                    </select>
                  </div>
                  <label style="margin-right: 15px" class="st-font" for="sex">Sex </label>
                  <div class="select-wrapper" style="margin-right: 15px">            
                    <select style="font-size: 20px" name="sex" id="sex" v-model="credentials.sex" class="st-font">
                      <option :value="sex" v-for="(sex, idx) in this.$store.state.sex" :key="idx">{{ sex }}</option>
                    </select>
                  </div>

                  <div class="control-group">
                      <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                          <label for="email">Email</label>
                          <input style="font-size: 30px" v-model.trim="credentials.email" class="form-control" id="email" type="text" placeholder="email" required="required" data-validation-required-message="Please enter your email address." />
                          <h6>정확한 e-mail을 작성해주세요.</h6>
                          <p class="help-block text-danger"></p>
                      </div>
                  </div>
                  <div class="control-group">
                      <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                          <label>password</label>
                          <input style="font-size: 30px" v-model.trim="credentials.password" class="form-control" id="password" type="password" placeholder="Password" required="required" data-validation-required-message="Please enter your password." />
                          <h6>password는 8자 이상을 권장합니다.</h6>
                          <p class="help-block text-danger"></p>
                      </div>
                  </div>
                  <div class="control-group">
                      <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                          <label>passwordConfirmation</label>
                          <input style="font-size: 30px" v-model.trim="credentials.passwordConfirmation" @keypress.enter="signUp" class="form-control" id="passwordConfirmation" type="password" placeholder="passwordConfirmation" required="required" data-validation-required-message="Please confirm your password" />
                          <h6>password는 8자 이상을 권장합니다.</h6>
                          <p class="help-block text-danger"></p>
                      </div>
                  </div>
                  <br />
                  <div id="success"></div>
                  <div class="text-white st-font form-group"><button @click="signUp" class="btn btn-secondary btn-xl" id="Signup" type="submit">Signup</button></div>
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
  name: "SignUp",
  data: function () {
    return {
      credentials: {
        username: '',
        age: '',
        sex: '',
        email: '',
        password: '',
        passwordConfirmation: '',
      },
    }
  },
  methods: {
    signUp: function () {
      axios.post(`${SERVER_URL}/accounts/signup/`, this.credentials)
      .then( () => {
        // console.log(res)
        this.$router.push({ name: "Login" })
        alert("가입을 축하드립니다....람쥐!")
      })
      .catch( (err) => {
        console.log(err)
      })
    },
  }
}
</script>

<style>

</style>
