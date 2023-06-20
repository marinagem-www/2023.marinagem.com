window.addEventListener("DOMContentLoaded", (_) => {
  new SimpleLightbox(".project-content img, .project-cover-container img", {
    sourceAttr: "src",
    overlayOpacity: 0.8,
    showCounter: false,
    loop: false,
  });
});
