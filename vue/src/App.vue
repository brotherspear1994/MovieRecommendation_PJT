<template>
  <div id="app" data-app>
    <img class="test margin_img" src="@/assets/지브리2.jpg">
    <Menu style="position:fixed; top:0; z-index:3;"></Menu>
    <router-view/>
    <footer class="footer">
      <br>
      <div>
        <h5 style="color: rgb(0,0,0)" class="text-center st-font">SSAFLIX</h5>
        <h5 style="color: rgb(0,0,0)" class="text-center st-font">Django & Vue.js</h5>
        <h5 style="color: rgb(0,0,0)" class="text-center title-font">서울 3반 4기 신상훈과 이형창</h5> 
        <img style="padding-bottom: 10px; color: rgb(0,0,0)" src="@/assets/sample22.png" height="100" width="180" class="img">
      </div>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'
import Menu from '@/components/Menu'


const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "App",
  components: {
    Menu,
  },
  methods: {
    getMovies: function () {
      axios.get(`${SERVER_URL}/movies/`)
      .then( (res) => {
        if (this.$store.state.movies.length === 0) {
          this.$store.state.movies = res.data
        }
      })
      .catch( (err) => {
        console.log(err)
      })
    },
  },
}
</script>

<style>
.footer {
  background-image: url("../src/assets/footer_sub.png");
  background-size: 100% 100%;
  /* background-color: #ffffff; */
  /* background-color: rgba(0.4) */
  /* background: transparent; */
  
}
.select-wrapper {
    display:inline-block;
    border:1px solid #bbbbbb;
    position:relative;
    width:120px;
    -webkit-border-radius:5px;
    -moz-border-radius:5px;
    border-radius:5px;
    margin-top: 10px;
}
.select-wrapper:before{
    content: "";
    position:absolute;
    right: 5px;
    top:8px;
    border-width: 5px 5px 5px 5px;
    border-style: solid;
    border-color: #666666 transparent  transparent  transparent ;
    z-index:3;
}
.select-wrapper:after {
    content:"";
    display:block;
    position:absolute;
    top:0px;
    bottom:0px;
    width:20px;
    right:0px;
    border-left:1px solid #bababa;
    background-color:#ededed;
    -webkit-border-top-right-radius:5px;
    -moz-border-top-right-radius:5px;
    border-top-right-radius:5px;
    -webkit-border-bottom-right-radius:5px;
    -moz-border-bottom-right-radius:5px;
    border-bottom-right-radius:5px;
}
select {
    width:100%;
    background-color:#ededed;
    border:none;
    outline:none;
    padding:0px;
    margin:0px;
    position:relative;
}
.st-font {
  font-family: 'Cute Font', 'Nerko One', cursive;
  font-weight: bold;
  font-size: x-large;
}
.title-font {
  font-family: 'Goldman', 'Gugi', cursive;
}
.content-font {
  font-family: 'Gaegu', 'Nanum Pen Script', cursive;
}
.margin_img {
  margin-bottom: 100px;
}
.test {
  width: 100%;
  height: 400px;
  /* position: fixed; */
  top: 0px;
  left: 0px;
  z-index:2;
}
.main {
  /* margin-left: auto; margin-right: auto;
  display: block; */
  /* position: fixed; */
  width: 100%;
  height: 10%;
  object-fit: cover;
  top: 0px;
  left: 0px;
  z-index:2;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
