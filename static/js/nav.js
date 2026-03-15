// Smooth nav hide/show on scroll
document.addEventListener('DOMContentLoaded', function() {
  var lastScroll = 0;
  var navEl = document.querySelector('nav');

  window.addEventListener('scroll', function() {
    var curr = window.scrollY;
    if (curr > lastScroll && curr > 100) {
      navEl.style.transform = 'translateY(-100%)';
    } else {
      navEl.style.transform = 'translateY(0)';
    }
    lastScroll = curr;
  });
});
