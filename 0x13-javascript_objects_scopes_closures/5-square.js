#!/usr/bin/node

class Rectangle {
    constructor (w, h) {
        if (w <= 0 || h <= 0 || typeof h === "undefined" || typeof h === "undefined") { return;}
      this.width = w >= 0 ? w : NaN;
      this.height = h >= 0 ? h : NaN;;
    }

    print () {
        for (let i = 0; i < this.height; i++) {
          console.log('X'.repeat(this.width));
        }
    }

    rotate () {
        let x = this.width;
        this.width = this.height;
        this.height = x;
    }

    double () {
        this.width = this.width * 2;
        this.height = this.height * 2;
    }
}

class square extends Rectangle{
    constructor (size) {
        super(size, size);
    }
}
  
module.exports = Rectangle;
