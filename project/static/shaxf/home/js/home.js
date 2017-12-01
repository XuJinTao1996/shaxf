$(function(){
    swiper1()
})

function swiper1(){
    var mySwiper = new Swiper('.swiper-container', {
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