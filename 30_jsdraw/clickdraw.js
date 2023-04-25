//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

ctx.fillStyle = "pink";

//init global state var
var mode = "rect";

//var toggleMode = function(e) {
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode == "rect") {
        mode = "circ";
        buttonToggle.innerHTML = "Circle";
      } else { 
        mode = "rect";
        buttonToggle.innerHTML = "Rectangle";
      }
      console.log("toggled to " + mode);
}

var drawRect = function(e) {
  let mouseX = e.offsetX; 
  let mouseY = e.offsetY;
  ctx.fillRect(mouseX, mouseY, 100, 200);
  console.log("mouseclick registered at ", mouseX, mouseY);
}

//var drawCircle = function(e){
var drawCircle = (e) => {
    let mouseX = e.offsetX; 
    let mouseY = e.offsetY;
    ctx.fillStyle = "pink";
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 50, 0, 2 * Math.PI);
    ctx.fill();
    ctx.stroke();
    console.log("mouseclick registered at ", mouseX, mouseY);
}

//var draw = function(e) {
var draw = (e) => {
  if (mode == "rect") {
    drawRect(e);
  } else {
    drawCircle(e);
  }
}

//var wipeCanvas = function() {
var wipeCanvas = () => {
  ctx.clearRect(0, 0, c.width, c.height);
}

c.addEventListener("click", draw);

var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);

var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);



