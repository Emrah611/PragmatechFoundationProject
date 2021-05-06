/* window.addEventListener('scroll', () => {
    //document.querySelector('nav').clientHeight - blokun icinde elementin hundurluyu
    if (window.scrollY > window.innerHeight / 4 - document.querySelector('nav').clientHeight) {
        document.querySelector('nav').style.opacity = 1;
    } else {
        document.querySelector('nav').style.opacity = 0;
    }
    // getBoundingClientRect().top - gorunen hisseden elementin yuxari hissesine geder olan mesafe
    if ((window.innerHeight + window.scrollY) > document.querySelector('.first__main').getBoundingClientRect().top) {
        document.querySelector('.first__main').classList.add('_active')
    } else {
        document.querySelector('.first__main').classList.remove('_active')
    }
    if ((window.innerHeight + window.scrollY) > document.querySelector('.second__main').offsetTop + document.querySelector('.second__main').clientHeight / 3) {
        for (let i = 0; i < document.querySelectorAll('.second__main p').length; i++) {
            document.querySelectorAll('.second__main p')[i].classList.add('_active')
        }
    } else {
        for (let i = 0; i < document.querySelectorAll('.second__main p').length; i++) {
            document.querySelectorAll('.second__main p')[i].classList.remove('_active')
        }
    }
})
const header = () => {
    if (window.scrollY == 0) {
        document.querySelectorAll('.header').forEach(e => {
            e.classList.add('_active');
        })
    }
}
header(); */

// Animasiya olunacaq elementler
const animationItems = document.querySelectorAll('._anim');
const animationOnScroll = () => {
    if (animationItems.length > 0) {
        for (let i = 0; i < animationItems.length; i++) {
            // Animasiya ne zaman baslasin
            const animationStart = 4;
            // ekranin olcusu elementin olsunun 1/4 oldugda animasi aktivlessin
            let animationItemPoint = window.innerHeight - animationItems[i].offsetHeight / animationStart;
            // Eger scroll deyeri > sehifenin en basindan elemente geder olan mesafe - elementin 1/4 geder
            if ((pageYOffset > (animationItems[i].offsetTop - animationItemPoint)) && (pageYOffset < (animationItems[i].offsetTop + animationItems[i].offsetHeight))) {
                animationItems[i].classList.add('_active');
            } else {
                // Animasiyani  tekrarlanmamasi ucun sert
                if (!animationItems[i].classList.contains('_noRepeat')) {
                    animationItems[i].classList.remove('_active');
                }
            }
        }
    }
}
window.addEventListener('scroll', animationOnScroll);
// Sehife acilanda il section animasiyanin aktivlesmesi
animationOnScroll();