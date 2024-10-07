'use strict';

document.addEventListener('click', (e) => {
  if (e.target.closest('.btn-close')) {
    const flash = e.target.closest('[role="alert"]');
    flash.remove();
  }
});
