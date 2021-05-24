window.onscroll = function() { myFunction() };

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

function myFunction() {
    if (window.pageYOffset >= sticky) {
        navbar.classList.add("sticky")
    } else {
        navbar.classList.remove("sticky");
    }
}


// let images = document.querySelectorAll('.mySlides');
// let start = 0;
// images[start].style.display = 'block';

// document.querySelector('.next').addEventListener('click', () => {
//     if (start == images.length - 1) {
//         start = -1;
//     };
//     for (let i = 0; i < images.length; i++) {
//         images[i].style.display = 'none';
//     }
//     images[++start].style.display = 'block';
// })

// document.querySelector('.prev').addEventListener('click', () => {
//     start -= 1;
//     if (start < 0) {
//         start = images.length - 1;
//     }
//     for (let i = 0; i < images.length; i++) {
//         images[i].style.display = 'none';
//     }
//     images[start].style.display = 'block';
// })