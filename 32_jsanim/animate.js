var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var dvdButton = document.getElementById("dvd");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.strokeStyle = "#AA336A"
ctx.fillStyle = "pink";

var requestID; // init global var for use with animation frames

var radius = 0;
var growing = true;

var clear = function(e) {
    e.preventDefault(); //if the event does not get explicitly handled, its default action should not be taken as it normally would be
    ctx.clearRect(0, 0, c.width, c.height);
};

var dvdLogoSetup = function() {
    window.cancelAnimationFrame(requestID);
    var rectWidth = 600/5;
    var rectHeight = 400/5;

    var rectX = Math.random() * c.width;
    var rectY = Math.random() * c.height;

    var xVel = 2;
    var yVel = 2;

    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var dvdLogo = function() {
        ctx.clearRect(0, 0, c.width, c.height);
        ctx.fillRect(rectX, rectY, rectWidth, rectHeight)
        ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
        if (rectX > c.width - rectWidth || rectX < 0) {
            xVel = xVel * -1;
        };
        if (rectY > c.height - rectHeight || rectY < 0) {
            yVel = yVel * -1;
        };
        rectX += xVel;
        rectY += yVel;
        requestID = window.requestAnimationFrame(dvdLogo);
    };
    dvdLogo();
};
var drawDot = () => {

    if (requestID) {
        window.cancelAnimationFrame(requestID)
        console.log("Cancelled")
    }

    //wipe the canvas
    ctx.clearRect(0, 0, c.width, c.height);

    //repaint the circle
    console.log("drawing...")
    console.log("radius: " + radius)
    ctx.beginPath();
    ctx.arc(c.width/2, c.height/2, radius, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();

    if (growing) {
        radius++;
    }
    else {
        radius--;
    };

    if (radius == c.width/2) {
        growing = false;
        console.log("growing set to false")
    }
    if (radius == 0) {
        growing = true;
        console.log("growing set to true")
    };

    
    requestID = window.requestAnimationFrame(drawDot);

    /*

    ...and somewhere (when/where is the right time?)
    Update requestID to propagate the animation/
    You will need
    window.cancelAnimationFrame()
    window.requestAnimationFrame()
    */
};

var stopIt = () => {
    console.log("stopIt invoked...");
    /* YOUR CODE HERE
        ...to stop the animation
        You will need window.cancelAnimationFrame()
    */
    window.cancelAnimationFrame(requestID)
    console.log("cancelID: " + requestID)
};

dotButton.addEventListener("click", drawDot);
dvdButton.addEventListener("click", dvdLogoSetup);
stopButton.addEventListener("click", stopIt);