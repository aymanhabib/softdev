var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "pink";

var requestID; // init global car for use with animation frames

var clear = (e) => {
    ctx.clearRect(0, 0, c.width, c.height);
};

var radius = 0;
var growing = true;

var drawDot = () => {
    clear(e);
    ctx.arc(c.width/2, c.height/2, radius, 0, 2 * Math.PI);
    ctx.fill();
    ctx.stroke();

    if (growing) {
        radius++;
    }
    else {
        radius--;
    };
    if (radius == c.width/2) {
        growing = false;
    }
    if (radius == 0) {
        growing = true;
    };

    window.cancelAnimationFrame();
    /*
    wipe the canvas,
    repaint the circle,

    ...and somewhere (when/where is the right time?)
    Updat requestID to propagate the animation/
    You will need
    window.cancelAnimationFrame()
    window.requestAnimationFrame()
    */
};

var growDot = () => {
    clear(e);
    ctx.arc(c.width/2, c.height/2, radius, 0, 2 * Math.PI);
    ctx.fill();
    ctx.stroke();
    radius++;
};

var shrinkDot = () => {

}
//var stopIt = function() {
var stopIt = () => {
    console.log("stopIt invoked...");
    console.log(requestID);
    /* YOUR CODE HERE
        ...to stop the animation
        You will need window.cancelAnimationFrame()
    */
};

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);