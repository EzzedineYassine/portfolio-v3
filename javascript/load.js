export function load() {
  return new Promise((resolve) => {
    const loader = document.getElementById('loader');
    const container = document.getElementById('container');

    if (container) {
      container.style.display = 'block';
    }

    if (loader) {
      loader.classList.add('fade-out-loader');
      setTimeout(() => {
        loader.style.display = 'none';
        loader.remove();
        resolve();
      }, 200);
    } else {
      resolve();
    }
  });
}
