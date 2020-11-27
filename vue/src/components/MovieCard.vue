<template>
  <div>
    <vue-glide v-if="movies.length"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{3000: {perView: 7}, 1100: {perView: 5}, 600: {perView: 3}}"
    >
      <vue-glide-slide
        v-for="(movie, idx) in movies"
        :key="idx">
        <MovieDetail 
          :movie="movie"
        />
        <!-- <p>{{ movie.title }}</p> -->
      </vue-glide-slide>
    </vue-glide>
    
  </div>
</template>

<script>
import { Glide, GlideSlide } from 'vue-glide-js'

import MovieDetail from "@/components/MovieDetail"

export default {
  name: "MovieCard",
  data: function () {
    return {
      show: false,
      variants: ["light", "dark"],
      headerBgVariant: "dark",
      headerTextVariant: "light",
      bodyBgVariant: "dark",
      bodyTextVariant: "light",
      footerBgVariant: "dark",
      footerTextVariant: "dark",
    }
  },
  props: {
    movies: {
      type: Array,
    }
  },
  components: {
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide,
    MovieDetail,
  },
  methods: {
    movieDetail: function () {
      this.show = true
    },
    close: function () {
      this.show = false
    }
  },
}
</script>


<style>
.w3-myfont {
  font-family: 'Luminari', fantasy;
}
.w2-myfont {
  font-family: 'Avantgarde', 'TeX Gyre Adventor', 'URW Gothic L', sans-serif;
}

#main {
padding: 4em 0 2em 0;
}

@media screen and (max-width: 736px) {

#main {
padding: 3em 0 1em 0;
}

}

#main .inner {
width: 90%;
max-width: 80em;
margin: 0 auto;
}

@media screen and (max-width: 480px) {

#main .inner {
width: 95%;
}
}
.thumbnails {
display: -moz-flex;
display: -webkit-flex;
display: -ms-flex;
display: flex;
-moz-align-items: stretch;
-webkit-align-items: stretch;
-ms-align-items: stretch;
align-items: stretch;
-moz-justify-content: center;
-webkit-justify-content: center;
-ms-justify-content: center;
justify-content: center;
-moz-flex-wrap: wrap;
-webkit-flex-wrap: wrap;
-ms-flex-wrap: wrap;
flex-wrap: wrap;
}

.thumbnails .box {
margin: 0 1em 2em 1em;
width: 30%;
}

@media screen and (max-width: 1280px) {

.thumbnails .box {
width: 45%;
}

}

@media screen and (max-width: 736px) {

.thumbnails .box {
width: 100%;
}

}
</style>
