var currSlide = 0;

function nextSlide() {
    ++currSlide;
    displayCurrSlide();
}

function prevSlide() {
    --currSlide;
    displayCurrSlide();
}

function displayCurrSlide() {
    var imgs = document.getElementsByClassName("comic_slide");
    console.log(imgs);
    currSlide %= imgs.length;
    if(currSlide < 0) currSlide = imgs.length - 1;
    console.log(currSlide)
    for(var i = 0; i != imgs.length; ++i) {
        imgs[i].style.display = "none";
    }
    imgs[currSlide].style.display = "block";
}