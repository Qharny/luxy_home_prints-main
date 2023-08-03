// searchPage fuction suspence
const cate = document.querySelectorAll('.cate-container');



// SUB MENU DISPLAY

let display = document.querySelector(".sub-menu")
let displaybtn = document.querySelector("#icon")

displaybtn.onclick = () => {
    display.classList.toggle('reveal');
}


// swiper
var swiper = new Swiper(".mySwiper", {
    slidesPerView: 3,
    spaceBetween: 30,
    slidesPerGroup: 3,
    loop: true,
    loopFillGroupWithBlank: false,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });


const none = document.querySelector(".fa-play, fa-solid");

none.onclick = () => {
  console.log("helloi");
}
