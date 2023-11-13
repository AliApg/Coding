let btn = document.querySelector(".click");
let body = document.querySelector("body");

btn.addEventListener("click", () => {
    body.classList.toggle("open");
});