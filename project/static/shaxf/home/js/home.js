$(function(){
    //首部轮播图
    swiper1()

    //轮播菜单
    swiper2()
})

function swiper1(){
    var mySwiper = new Swiper('#headerWheelList', {
        direction: 'horizontal',
        loop: true,
        speed:500,
        autoplay:2000,

               // 如果需要分页器
        pagination: {
            el: '.swiper-pagination',
        },
    })
}

function swiper2(){
    var mySwiper = new Swiper('#menuNavList', {
        slidesPerView: 3,
        paginationClickable: true,
        spaceBetween: 2,
        loop: false,
    })
}