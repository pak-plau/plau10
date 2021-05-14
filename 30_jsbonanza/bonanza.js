var c = document.getElementById("playground");
var playButton = document.getElementById("buttonPlay");
var resetButton = document.getElementById("buttonReset");

var ctx = c.getContext("2d");

ctx.fillStyle("#FF0000");

var requestID;

var clear = (e) => {
    console.log("clear invoked...")
    ctx.clearRect(0, 0, c.width, c.height);
};

