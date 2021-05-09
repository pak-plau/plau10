// Team javabean -- Pak Ming Lau, Eric Lo
// SoftDev pd1
// K27 -- canvas based JS animation with a dvd screensaver
// 2021-05-09

//access canvas and buttons via DOM
var c = document.getElementById("playground");// GET CANVAS
var dotButton = document.getElementById("buttonCircle");// GET DOT BUTTON
var stopButton = document.getElementById("buttonStop");// GET STOP BUTTON
var playButton = document.getElementById("buttonPlay");// GET PLAY BUTTON

//prepare to interact with canvas in 2D
var ctx = c.getContext("2d");

//set fill color to team color
ctx.fillStyle = "#FF0000";

var requestID;  //init global var for use with animation frames

//var clear = function(e) {
var clear = (e) => {
    console.log("clear invoked...")
    ctx.clearRect(0, 0, c.width, c.height);
};

var radius = 0;
var growing = true;

//var drawDot = function() {
var drawDot = () => {
    console.log("drawDot invoked...")

    window.cancelAnimationFrame(requestID);
    clear();
    ctx.beginPath(); //necessary for circles to disappear when cleared
    ctx.arc(c.width / 2, c.height / 2, radius, 0, 2 * Math.PI);
    ctx.fill();
    if(growing) {
        radius++;
        growing = radius <= c.width / 2; // if growing, then it should turn false when the max radius is exceeded
    }else {
        radius--;
        growing = radius <= 5; // if not growing, then it should turn back to true when the min radius is reached
    }
    requestID = window.requestAnimationFrame(drawDot);
};

//image variable
var logo = new Image();
logo.src = "logo_dvd.jpg";
//starting coords
var x = c.width / 2;
var y = c.height / 2;
//speed
var dx = 1;
var dy = 1;

//var play = function() {
var drawDVD = () => {
    console.log("drawDVD invoked...");

    window.cancelAnimationFrame(requestID);
    clear();
    ctx.drawImage(logo, x, y, 100, 50); //image obj, x and y cord, width and height of logo

    if (x + 100 >= c.width || x <= 0) { //left and right wall collision
        dx *= -1;
    }
    if (y + 50 >= c.height || y <= 0) { //top and bot wall collision
        dy *= -1;
    }

    x += dx;
    y += dy;

    requestID = window.requestAnimationFrame(drawDVD);
};

//var stopIt = function() {
var stopIt = () => {
    console.log("stopIt invoked...")
    console.log( requestID );
    window.cancelAnimationFrame(requestID);
};

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
playButton.addEventListener("click", drawDVD);