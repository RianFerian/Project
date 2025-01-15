function Snake() {
    this.x = 0;
    this.y = 0;
    this.xspeed = 1;
    this.yspeed = 0;
    this.total = 0;
    this.tail = [];
    this.score = 1;
    this.level = 10;

    this.eat = function(pos){
        var d = dist(this.x, this.y, pos.x, pos.y);
        if (d < 1){
            this.total++;
            this.score++;
            if (this.score % 15 === 0){
                this.level++;
            }
            return true;

        } else {
            return false;
        }

    }

    this.dir = function(x,y){
        this.xspeed = x;
        this.yspeed = y;
    }

    this.death = function(){
        // Check if the snake hits the walls or its own tail
        if (this.x < 0 || this.x >= width || this.y < 0 || this.y >= height) {
            return true;
        }
        for (let i = 0; i < this.tail.length; i++) {
            if (this.x === this.tail[i].x && this.y === this.tail[i].y) {
                return true;
            }
        }
        return false;
    }
    

    this.restart = function(){
        this.total = 0;
        this.score = 0;
        this.level = 10;
        this.tail = [];
        this.x = floor(random(floor(30))) * scl;
        this.y = floor(random(floor(20))) * scl;

    }

    this.update = function(){
        for (var i = 0; i < this.tail.length - 1; i++) {
            this.tail[i] = this.tail[i + 1];
        }
        if (this.total >= 1) {
            this.tail[this.total - 1] = createVector(this.x, this.y);
        }
        
        this.x = this.x + this.xspeed*scl;
        this.y = this.y + this.yspeed*scl;

        // Check if the snake hits the edges (left, right, top, bottom)
        if (this.x < 0 || this.x >= width || this.y < 0 || this.y >= height) {
            gameOver(); // Reset the game if snake hits the edges
        }

    }

    this.show = function() {
        for (var i = 0; i < this.tail.length; i++) {
            // Calculate a gradient from blue (light) to dark blue
            let blue = map(i, 0, this.tail.length, 255, 125); // Gradient for blue channel
            fill(0, 0, blue); // Red and Green channels are 0, Blue channel varies
            rect(this.tail[i].x, this.tail[i].y, scl, scl);
        }
    
        // Draw the head of the snake
        fill(0, 0, 100); // Solid blue for the head
        rect(this.x, this.y, scl, scl);
    };
}

