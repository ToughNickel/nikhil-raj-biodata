// Cycling greeting text — reads from Django-injected JSON
document.addEventListener('DOMContentLoaded', function() {
  var dataEl = document.getElementById('greetings-data');
  if (!dataEl) return;

  var greetings = JSON.parse(dataEl.textContent);
  if (!greetings || greetings.length === 0) return;

  var gIdx = 0;
  var greetEl = document.getElementById('greeting-text');
  if (!greetEl) return;

  greetEl.style.transition = 'opacity 0.3s ease';

  setInterval(function() {
    gIdx = (gIdx + 1) % greetings.length;
    greetEl.style.opacity = 0;
    setTimeout(function() {
      greetEl.textContent = greetings[gIdx];
      greetEl.style.opacity = 1;
    }, 300);
  }, 2500);
});
