//
$(function () {
    //selecciona todos los elementos con la clase sidebar-link, se le asigna un click
    $(".sidebar-link").click(function () {
        $(".sidebar-link").removeClass("is-active");
        $(this).addClass("is-active");
    });
});
//redimenciona la ventana del navegador 
$(window)
    .resize(function () {
        if ($(window).width() > 1090) {
            $(".sidebar").removeClass("collapse");
        } else {
            $(".sidebar").addClass("collapse");
        }
    })
    .resize();
//obtiene los elementos con la clase (video)
const allVideos = document.querySelectorAll(".video");

//a los elementos con de la lista de videos, se le asigna "mousover" y "mousleave"
allVideos.forEach((v) => {
    v.addEventListener("mouseover", () => {
        const video = v.querySelector("video");
        video.play();
    });
    v.addEventListener("mouseleave", () => {
        const video = v.querySelector("video");
        video.pause();
    });
});

$(function () {
    //se le asigna un evento de clic a los elementos con las clases "logo" , "logo-expand" y "discover"
    $(".logo, .logo-expand, .discover").on("click", function (e) {
        $(".main-container").removeClass("show");
        $(".main-container").scrollTop(0);
    });
    // Asigna un evento de clic a los elementos con las clases "trending" y "video"
    $(".trending, .video").on("click", function (e) {
        $(".main-container").addClass("show");
        $(".main-container").scrollTop(0);
        $(".sidebar-link").removeClass("is-active");
        $(".trending").addClass("is-active");
    });
     // Asigna un evento de clic a los elementos con la clase "video"
    $(".video").click(function () {
        var source = $(this).find("source").attr("src");
        var title = $(this).find(".video-name").text();
        var person = $(this).find(".video-by").text();
        var img = $(this).find(".author-img").attr("src");
        $(".video-stream video").stop();
        $(".video-stream source").attr("src", source);
        $(".video-stream video").load();
        $(".video-p-title").text(title);
        $(".video-p-name").text(person);
        $(".video-detail .author-img").attr("src", img);
    });
});

document.addEventListener("click", function(event) {
    var userMenu = document.querySelector(".user-menu");
    var dropdownMenu = document.querySelector(".dropdown-menu");
    var arrowDown = document.querySelector(".arrow-down");
  
    if (!userMenu.contains(event.target)) {
      dropdownMenu.classList.remove("show");
      arrowDown.classList.remove("rotate");
    } else {
      dropdownMenu.classList.toggle("show");
      arrowDown.classList.toggle("rotate");
    }
  });