// Set variables
let root = document.documentElement;
let slider = document.body.querySelector("#slider");

slider.addEventListener("input", evt => {
  root.style.setProperty("--r",slider.value);
});
