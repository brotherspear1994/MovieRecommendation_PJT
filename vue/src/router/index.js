import Vue from 'vue'
import VueRouter from 'vue-router'
import Community from '@/views/community/Community'
import CommunityDetail from '@/views/community/CommunityDetail'
import CommunityDetailUpdate from '@/views/community/CommunityDetailUpdate'
import Recommend from '@/views/home/Recommend'
import Intro from '@/views/home/Intro'
import Users from '@/views/accounts/Users'
import SignUp from '@/views/accounts/SignUp'
import Login from '@/views/accounts/Login'
import MyProfile from '@/views/accounts/MyProfile'
import Profile from '@/views/accounts/Profile'
// import Review from '@/views/reviews/Review'
// import ReviewDetail from '@/views/reviews/ReviewDetail'
// import ReviewUpdate from '@/views/reviews/ReviewUpdate'

Vue.use(VueRouter)

const routes = [
  {
    path: '/community',
    name: 'Community',
    component: Community,
  },
  {
    path: '/communitydetail/:community_pk',
    name: 'CommunityDetail',
    component: CommunityDetail,
  },
  {
    path: '/communitydetail/update/:community_pk',
    name: 'CommunityDetailUpdate',
    component: CommunityDetailUpdate,
  },
  {
    path: '/',
    name: 'Intro',
    component: Intro,
  },
  {
    path: '/recommend',
    name: 'Recommend',
    component: Recommend,
  },
  {
    path: '/users',
    name: 'Users',
    component: Users,
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/myprofile',
    name: 'MyProfile',
    component: MyProfile,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
  },
  // {
  //   path: '/review',
  //   name: 'Review',
  //   component: Review,
  // },
  // {
  //   path: '/reviewdetail/:review_pk',
  //   name: 'ReviewDetail',
  //   component: ReviewDetail,
  // },
  // {
  //   path: '/reviewdetail/update/:review_pk',
  //   name: 'ReviewUpdate',
  //   component: ReviewUpdate,
  // },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
