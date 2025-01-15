var s;
var scl=20;
var food;
var score;

function setup(){
    let canvas = createCanvas(600, 400);
    canvas.parent("canvas-container"); // Attach canvas to the container
    s = new Snake();
    frameRate(s.level);
    pickLocation();
}

function pickLocation(){
    var cols = floor(width/scl);
    var rows = floor(height/scl);
    // Generate a random location for the food
    do {
        food = createVector(floor(random(cols)), floor(random(rows)));
        food.mult(scl);

        // Check if the food position collides with the snake
        var collision = false;
        for (var i = 0; i < s.tail.length; i++) {
            if (food.x === s.tail[i].x && food.y === s.tail[i].y) {
                collision = true;
                break;
            }
        }
        if (food.x === s.x && food.y === s.y) {
            collision = true;
        }
    } while (collision);
}

// Function to update score and level in the DOM
function updateInfo() {
    document.getElementById("score").textContent = `Score: ${s.score}`;
    document.getElementById("level").textContent = `Level: ${s.level-9}`;
}

function gameOver(){
    s.restart();
    pickLocation();
    updateInfo();
}

function draw(){
    background(51);
    
    if (s.eat(food)){
        pickLocation();
        updateInfo();
    }
    if (s.death()){
        gameOver();
    }
    s.update();
    s.show();

    fill(0, 255, 100);
    rect(food.x, food.y, scl, scl);

    // // Display score
    // fill(0);
    // textSize(16);
    // text("Score: " + s.score, 10, 20);
}

let currentDirection = { x: 1, y: 0 }; // Initial direction, e.g., moving right

function keyPressed() {
    if (keyCode === UP_ARROW && currentDirection.y === 0) {
        s.dir(0, -1)*s.level; // Move up
        currentDirection = { x: 0, y: -1 };
    } else if (keyCode === DOWN_ARROW && currentDirection.y === 0) {
        s.dir(0, 1)*s.level; // Move down
        currentDirection = { x: 0, y: 1 };
    } else if (keyCode === RIGHT_ARROW && currentDirection.x === 0) {
        s.dir(1, 0)*s.level; // Move right
        currentDirection = { x: 1, y: 0 };
    } else if (keyCode === LEFT_ARROW && currentDirection.x === 0) {
        s.dir(-1, 0)*s.level; // Move left
        currentDirection = { x: -1, y: 0 };
    }
}
