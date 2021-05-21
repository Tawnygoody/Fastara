$(document).ready(function(){
    $(".sidenav").sidenav({edge:"right"});
    $('.modal').modal();
    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: true
    }, setTimeout(autoplay, 4000));
    AOS.init(); // Initilizes on-scroll library
  });

  function autoplay() { // Help with autoplay for carousel taken from https://stackoverflow.com/questions/36581504/materialize-carousel-slider-autoplay
      $('.carousel').carousel('next');
      setTimeout(autoplay, 5000);
  }