const TARGET_PATHS = [
  "/blog/2025/pyconjp-2025/speaker/",
]
const SCALE_SIZE = 0.9;

function resizeContent(target, width, height, rate) {
  const slide = target.querySelector('iframe');
  const scale = target.clientWidth * rate / width;
  slide.width = width * scale;
  slide.height = height * scale;
}

function resize() {
  const slide = document.querySelector('iframe');
  resizeContent(slide.parentElement, slide.width, slide.height, SCALE_SIZE);
    const resizeObserver = new ResizeObserver(entries => {
      for (let entry of entries) {
        resizeContent(entry.target, slide.width, slide.height, SCALE_SIZE)
      }
    });
    resizeObserver.observe(slide.parentElement);
}


if (TARGET_PATHS.includes(location.pathname)) {
  if (document.readyState === "loading") {
    document.addEventListener('DOMContentLoaded', resize);
  } else {
    resize();
  }
}
document.addEventListener('htmx:afterSwap', resize);
