#!/usr/bin/node
let toFactorial = process.argv[2];
console.log(getFactorial(parseInt(toFactorial)));
function getFactorial (x) {
  if (isNaN(x) || x === 0) {
    return 1;
  } else if (x < 0) {
    return -1;
  }
  return (x * getFactorial(x - 1));
}
