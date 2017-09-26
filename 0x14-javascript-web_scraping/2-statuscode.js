#!/usr/bin/node
// Script to display the status of a GET request
const request = require('request');
const requestURL = process.argv[2];

request(requestURL, function (error, response, body) {
  console.log('code: ', response.statusCode);
  if (error) {
    console.log(error);
  }
});
