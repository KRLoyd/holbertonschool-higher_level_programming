#!/usr/bin/node
// Script to import an array and compute a new array
const list = require('./100-data').list;

let index = 0;

let computedList = list.map(function (x) {
  let newItem = x * index;
  index += 1;
  return newItem;
});

console.log(list);
console.log(computedList);
