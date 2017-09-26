#!/usr/bin/node
// Script to read and print the content of a file
// If an error occurs while reading, the error object is printed
const fs = require('fs');
let passedFile = process.argv[2];
console.log('passedFile: ' + passedFile);
fs.readFile(passedFile, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
