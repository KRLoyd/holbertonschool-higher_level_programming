#!/usr/bin/node
let squareSize = process.argv[2];
let squareRow = getSquareRow(squareSize);
if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < squareSize; i++) {
    console.log(squareRow);
  }
}
function getSquareRow (size) {
  let tempRow = 'x';
  for (let i = 0; i < size - 1; i++) {
    tempRow += 'x';
  }
  return tempRow;
}
