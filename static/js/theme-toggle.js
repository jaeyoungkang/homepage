(function () {
  var KEY = 'yc-theme';
  var root = document.documentElement;
  var buttons = document.querySelectorAll('.theme-toggle button[data-theme-set]');

  function applyTheme(theme) {
    if (theme !== 'editorial' && theme !== 'studio') return;
    root.setAttribute('data-theme', theme);
    try { localStorage.setItem(KEY, theme); } catch (e) {}
    buttons.forEach(function (btn) {
      var pressed = btn.getAttribute('data-theme-set') === theme;
      btn.setAttribute('aria-pressed', pressed ? 'true' : 'false');
    });
  }

  var current = root.getAttribute('data-theme') || 'editorial';
  buttons.forEach(function (btn) {
    btn.setAttribute('aria-pressed', btn.getAttribute('data-theme-set') === current ? 'true' : 'false');
    btn.addEventListener('click', function () {
      applyTheme(btn.getAttribute('data-theme-set'));
    });
  });

  function syncEyebrow() {
    var theme = root.getAttribute('data-theme');
    document.querySelectorAll('.ed-only').forEach(function (el) {
      el.style.display = theme === 'editorial' ? '' : 'none';
    });
    document.querySelectorAll('.st-only').forEach(function (el) {
      el.style.display = theme === 'studio' ? '' : 'none';
    });
  }
  syncEyebrow();
  var observer = new MutationObserver(syncEyebrow);
  observer.observe(root, { attributes: true, attributeFilter: ['data-theme'] });
})();
