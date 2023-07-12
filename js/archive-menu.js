window.addEventListener("DOMContentLoaded", (_) => {
  const orgOptions = Array.from(document.getElementsByClassName("org-option"));

  orgOptions.forEach(o => {
    o.addEventListener("click", () => {
      orgOptions.forEach(o2 => o2.classList.remove("selected"));
      o.classList.add("selected");
    });
  });
  orgOptions[0].click();
});
