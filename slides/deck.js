(function () {
  const slides = [...document.querySelectorAll('.slide')];
  let i = 0;
  function show(n) {
    i = Math.max(0, Math.min(slides.length - 1, n));
    slides.forEach((s, k) => s.classList.toggle('on', k === i));
    document.getElementById('bar').style.width =
      ((i + 1) / slides.length * 100) + '%';
    document.getElementById('num').textContent = (i + 1) + ' / ' + slides.length;
    try { location.hash = i + 1; } catch (e) {}
  }
  addEventListener('keydown', e => {
    const k = e.key;
    if (['ArrowRight', ' ', 'PageDown', 'ArrowDown'].includes(k)) { show(i + 1); e.preventDefault(); }
    else if (['ArrowLeft', 'PageUp', 'ArrowUp'].includes(k)) { show(i - 1); e.preventDefault(); }
    else if (k === 'Home') show(0);
    else if (k === 'End') show(slides.length - 1);
    else if (k.toLowerCase() === 'f') {
      document.fullscreenElement ? document.exitFullscreen()
                                 : document.documentElement.requestFullscreen?.();
    }
  });
  addEventListener('click', e => {
    if (!e.target.closest('pre,table,a')) show(i + 1);
  });
  show(parseInt(location.hash.slice(1)) - 1 || 0);
})();
