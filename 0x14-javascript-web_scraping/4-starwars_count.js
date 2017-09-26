#!/usr/bin/node
// Script to print the number of times character "Wedge Antilles" is present
const request = require('request');
const characterToFind = 'https://swapi.co/api/people/18/';
let requestURL = process.argv[2];

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let theBody = JSON.parse(body);
    let movieResults = theBody.results;
    let count = 0;
    for (let movieCount = 0;
       movieCount < theBody.count;
       movieCount++) {
      if (movieResults[movieCount].characters.includes(characterToFind)) {
        count = count + 1;
      }
    }
    console.log(count);
  }
});
