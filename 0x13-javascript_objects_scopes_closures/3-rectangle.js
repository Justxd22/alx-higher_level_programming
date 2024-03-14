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
  }
  
module.exports = Rectangle;
