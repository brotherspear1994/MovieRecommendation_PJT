<template>
  <div>
    <CreateReview 
      @reviews-updated="reviewsUpdated"
      :movie="movie"
      style="margin-bottom:30px"
    />
    <ReviewList 
      :reviews="reviews"
      :movie="movie"
      @deleteReview="getReviews"
      @reviews-updated="reviewsUpdated"
    />
  </div>
</template>

<script>
import ReviewList from '@/components/ReviewList'
import CreateReview from '@/components/CreateReview'

import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Review',
  components: {
    CreateReview,
    ReviewList,
  },
  props: {
    movie: {
      type: Object,
    }
  },
  data: function () {
    return {
      reviews: [],
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
    getReviews: function () {
      const config = this.getToken()

      axios.get(`${SERVER_URL}/movies/${this.movie.id}/review_list_create/`, config)
      .then((res) => {
        // console.log(res)
        this.reviews = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    reviewsUpdated: function () {
      this.getReviews()
    },
  },
  created: function () {
    this.getReviews()
  },
}
</script>

<style>

</style>
