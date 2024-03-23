#!/usr/bin/node

const Square = require("./4-rectangle");

class square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
