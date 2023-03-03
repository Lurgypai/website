// https://stackoverflow.com/questions/247483/http-get-request-in-javascript

// asynchronous get request to endpoint (theUrl), invoked on callback
function httpGetAsync(theUrl, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
      if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
          callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous
    xmlHttp.send(null);
}

var pageCount = 0;
var currSlide = 0;

function nextSlide() {
    ++currSlide;
    if(currSlide == pageCount) currSlide = 0;
    displayText();
}

function prevSlide() {
    --currSlide;
    if(currSlide < 0) currSlide = pageCount - 1;
    displayText();
}

function displayTextCallback(data) {
          document.getElementById("content").innerHTML =
      "<p class=\"text fade_in\">" + data +
      "</p>";
}

function displayText() {
    httpGetAsync("http://yollotl.xyz/content/" + currSlide + ".txt", displayTextCallback);
    document.getElementById("title").innerHTML = 
    "<p class =\"text_title fade_in\">" + currSlide + "</p>"

    document.getElementById("content").innerHTML =
    "<p class =\"text\">...</p>"
}

function displayAbout() {
    currSlide = -1;
    httpGetAsync("http://yollotl.xyz/content/about.txt", displayTextCallback);
    document.getElementById("title").innerHTML = 
    "<p class =\"text_title fade_in\">About</p>"

    document.getElementById("content").innerHTML =
    "<p class =\"text\">...</p>"
}

function displayLandingCallback(data) {
    j = JSON.parse(data)
    pageCount = j['count'] - 1 // remove about
    currSlide = pageCount - 1
    document.getElementById("title").innerHTML =
    "<p class =\"text_title fade_in\">" + currSlide + "</p>"

    document.getElementById("content").innerHTML =
    "<p class=\"text fade_in\">" + j['content'] +
    "</p>";
}

function displayLanding() {
    httpGetAsync("http://yollotl.xyz/e/landing", displayLandingCallback);
}