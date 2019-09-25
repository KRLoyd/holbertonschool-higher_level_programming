#!/usr/bin/node
// Script to get the contents of a webpage and store it in a file
// URL to request is the first passed argument
// file path is the second passed argument
const fs = require('fs');
const request = require('request');

const requestURL = process.argv[2];
const fileName = process.argv[3];

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(fileName, body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
