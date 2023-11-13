const close = document.querySelector(".close");
const btn = document.querySelector(".click");
const sideNav = document.querySelector(".main-nav");

btn.addEventListener("click", () => {
    btn.classList.toggle('open');
    close.classList.toggle('clicked');
    sideNav.classList.toggle('clicked');
});

$('.menu-main li').hover(function () {
    $('.menu-sub', this).toggleClass('open', 500);
});

close.addEventListener("click", () => {
    btn.classList.remove('open');
    close.classList.remove('clicked');
    sideNav.classList.remove('clicked');
});

const navBar = document.querySelector(".container");
const start = document.querySelector(".start");

const up = document.querySelector("#up");

up.addEventListener("click", () => {
    window.scrollTo(0,0);
});

function down() {
    window.scrollTo(0, document.documentElement.scrollHeight);
}

const openerPicOptions = {
    rootMargin: "-70px 0px 0px 0px"
    // threshold: .1
};

const openerPicObserver = new IntersectionObserver(function (entries, openerPicObserver) {
    entries.forEach(entry => {
        if (!entry.isIntersecting) {
            navBar.classList.add("scrolled");
            up.classList.add("scrolled");
        } else {
            navBar.classList.remove("scrolled");
            up.classList.remove("scrolled");
        }
    })
}, openerPicOptions);

openerPicObserver.observe(start);

const fader = document.querySelectorAll(".information")
const slider = document.querySelectorAll(".sub-description");

const faderOptions = {
    rootMargin: "0px 0px -15% 0px"
};

const appearOnScroll = new IntersectionObserver(function (entries, appearOnScroll) {
    entries.forEach(entry => {
        if (!entry.isIntersecting) {
            return
        } else {
            entry.target.classList.add("arrives");
            appearOnScroll.unobserve(entry.target)
        }
    })
}, faderOptions);

fader.forEach(fade => {
    appearOnScroll.observe(fade)
});

slider.forEach(slide => {
    appearOnScroll.observe(slide)
})