import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],

    communities: [],

    sex: ["male", "female"],
    ages: ["10대", "20대", "30대", "40대", "50대", "60대", "70대", "80대", "90대",],


    reviewRate: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    login: false
  },
  mutations: {
    CREATE_Detail_Community: function (state, community) {
      state.communities.push(community)
    },
    CREATE_REVIEW: function (state, review) {
      state.reviews.push(review)
    },
    LOGIN_CHANGE: function (state, loginStatus) {
      // console.log(loginStatus)
      if (loginStatus) {
        state.login = true
        console.log(state.login)
      }
      else {
        state.login = false
      }
    }
  },
  actions: {
    createDetailCommunity: function ({commit}, community) {
      commit('CREATE_Detail_Community', community)
    },
    createReview: function ({ commit }, review) {
      commit("CREATE_REVIEW", review)
    },
    loginChange: function({commit}, loginStatus) {
      commit("LOGIN_CHANGE", loginStatus)
    },
  },
  modules: {
  },
  plugins: [
    createPersistedState()
  ]
})

