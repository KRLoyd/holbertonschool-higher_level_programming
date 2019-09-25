#!/usr/bin/node
// Function to print the number of args already printed and the new arg
let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count += 1;
};
