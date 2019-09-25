#!/usr/bin/node
// Define class Square
// Inherits from class Square of 5-square.js
module.exports = {Square: Square};

const parentSquare = require('./5-square').Square;

function Square (size) {
  parentSquare.call(this, size);
}

Square.prototype.charPrint = function (c) {
  if (c === undefined) {
    c = 'X';
  }
  for (let i = 0; i < this.height; i++) {
    console.log(c.repeat(this.width));
  }
};
