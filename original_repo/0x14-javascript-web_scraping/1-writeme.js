#!/usr/bin/node
// Script to write a string to a file
// If an error occurs while writing, the error object is printed
const fs = require('fs');
let fileName = process.argv[2];
let stringToWrite = process.argv[3];

fs.writeFile(fileName, stringToWrite, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
