#!/usr/bin/node
// Define Class Square
// Inherits from Rectangle of 4-rectangle.js
module.exports = {Square: Square};

const Rectangle = require('./4-rectangle').Rectangle;

function Square (size) {
  Rectangle.call(this, size, size);
}
