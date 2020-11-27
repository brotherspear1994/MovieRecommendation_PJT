<template>
  <div>
    <section class="page-section bg-secondary text-white mb-0" id="about">
        <div class="container">
            <h2 class="page-section-heading text-center text-uppercase text-white title-font" style="margin-bottom:60px; margin-top: 60px">SSAFY 4기 서울 3반 / SSAFLIX 팀을 소개합니다!</h2>
            <div class="divider-custom divider-light">
                <div class="divider-custom-line"></div>
                <div class="divider-custom-icon"><i class="fas fa-fire-alt"></i></div>
                <div class="divider-custom-line"></div>
            </div>
            <div class="text-center mt-4 content-font">
                <button @click="moveToHome" class="btn btn-xl btn-outline-light">
                    <i class="fas fa-play mr-2"></i>
                    Go Login!
                </button>
            </div>
            <!-- About Section Content-->
            <div class="row">
                <img src="@/assets/sample22.png" height="190" width="380" class="img">
            </div>
            <div class="title-font">
                <div class="mx-auto" style="margin-bottom:40px"><h1 class="page-section-heading text-center text-uppercase text-white">최고의 영화 추천 웹 서비스 SSAFLIX !!</h1></div>
                <div class="mx-auto"><video style="width: 1000px; height: 600px;" autoplay loop src="@/assets/movie_list.mp4"></video></div>
                <div class="mx-auto" style="margin-top:40px; margin-bottom:40px"><h2 class="page-section-heading text-center text-uppercase text-white">SSAFLIX는 5가지 방식으로 영화를 추천해드립니다 !</h2></div>
                <h5 style="margin-left:18%;" class="page-section-heading text-left text-uppercase text-white content-font">1. 랜덤 영화 추천</h5>
                <h5 style="margin-left:18%;" class="page-section-heading text-left text-uppercase text-white content-font">2. 평점 순 영화 추천</h5>
                <h5 style="margin-left:18%;" class="page-section-heading text-left text-uppercase text-white content-font">3. 짧은 상영시간 순 영화 추천</h5>
                <h5 style="margin-left:18%;" class="page-section-heading text-left text-uppercase text-white content-font">4. 리뷰 순 유사 장르 영화 추천</h5>
                <h5 style="margin-left:18%;" class="page-section-heading text-left text-uppercase text-white content-font">5. 사용자 좋아요를 반영한 맞춤형 빅데이터 영화 추천</h5>
                <div class="mx-auto"><video style="width: 1000px; height: 600px;" autoplay loop src="@/assets/menu_tab2.mp4"></video></div>
                <div class="mx-auto" style="margin-top:40px; margin-bottom:40px"><h2 class="page-section-heading text-center text-uppercase text-white">왼쪽 메뉴 탭을 이용해 SSAFLIX의 다양한 기능을 만나보세요 !</h2></div>
                <div class="mx-auto"><video style="width: 1000px; height: 600px;" autoplay loop src="@/assets/info_review.mp4"></video></div>
                <div class="mx-auto" style="margin-top:40px; margin-bottom:40px"><h2 class="page-section-heading text-center text-uppercase text-white">재밌게 본 영화의 리뷰를 작성해주세요 !</h2></div>
                <div class="mx-auto"><video style="width: 1000px; height: 600px;" autoplay loop src="@/assets/community_use.mp4"></video></div>
                <div class="mx-auto" style="margin-top:40px; margin-bottom:40px"><h2 class="page-section-heading text-center text-uppercase text-white">Community 게시판을 이용해 다른 사용자와 의견을 나누세요 !</h2></div>
                <div class="mx-auto"><video style="width: 1000px; height: 600px;" autoplay loop src="@/assets/moving_menu.mp4"></video></div>
                <div class="mx-auto" style="margin-top:40px; margin-bottom:40px"><h2 class="page-section-heading text-center text-uppercase text-white">다른 사용자들이 좋아요 한 영화를 찾아보세요 !</h2></div>
                <div class="mx-auto"><video style="width: 1000px; height: 600px;" autoplay loop src="@/assets/otherprofile2.mp4"></video></div>
                <div class="mx-auto" style="margin-top:40px; margin-bottom:40px"><h2 class="page-section-heading text-center text-uppercase text-white">팔로우 기능을 통해 내 취향의 영화를 쉽게 찾아보세요 !</h2></div>
                <div class="mx-auto"><h2 class="page-section-heading text-center text-uppercase text-white">지금 바로 SSAFLIX를 시작하세요 !</h2></div>
            </div>
            <!-- About Section Button-->
            <div class="text-center mt-4">
                <button @click="moveToHome" class="btn btn-xl btn-outline-light content-font" style="margin-top: 50px; margin-bottom: 50px">
                    <i class="fas fa-play mr-2"></i>
                    Go Login!
                </button>
            </div>
        </div>
    </section>
  </div>
</template>

<script>
export default {
    name: "Intro",
    methods: {
        moveToHome: function () {
            this.$router.push({name: 'Login'})
        }
    }

}
</script>

<style>
.img {
    display: block;
    margin: auto;
}
</style>
