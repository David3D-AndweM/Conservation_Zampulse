
    document.addEventListener("DOMContentLoaded", function() {
    const stories = document.querySelectorAll('.story-card');
    let currentIndex = 0;

    function showNextStory() {
    stories[currentIndex].classList.remove('active');
    currentIndex = (currentIndex + 1) % stories.length;
    stories[currentIndex].classList.add('active');
}

    setInterval(showNextStory, 3000); // Change story every 3 seconds
});

var swiper = new Swiper('.blog-slider', {
  spaceBetween: 30,
  effect: 'fade',
  loop: true,
  mousewheel: {
    invert: false,
  },
  pagination: {
    el: '.blog-slider__pagination',
    clickable: true,
  }
});
