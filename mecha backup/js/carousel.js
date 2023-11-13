
const carousel = document.querySelectorAll(".carousel>input");
const prjct = document.querySelector(".Prjct").style;

var time;

function move() {
    clearInterval(time);
    timer();
    setTimeout(function () {

        if (carousel[0].checked) {

            prjct.display = "flex";

        } else {

            prjct.display = "none";

        }
    }, 50);
}

function timer() {
    time = setInterval(function () {
        for (var i = 0; i != carousel.length; i++) {
            if (carousel[i].checked) {
                try {
                    carousel[i + 1].checked = true;
                    prjct.display = "none";
                } catch {
                    carousel[0].checked = true;
                    prjct.display = "flex";
                }
                break;
            }
        }
    }, 6000);
}

timer();

