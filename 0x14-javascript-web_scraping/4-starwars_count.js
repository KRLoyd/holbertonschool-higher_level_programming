#!/usr/bin/node
// Script to print the number of times character "Wedge Antilles" is present
const request = require('request');
const characterToFind = 'https://swapi.co/api/people/18/';
let requestURL = 'http://swapi.co/api/films/';

request(requestURL, function (error, response, body) {
  let theBody = JSON.parse(body);
  let movieResults = theBody.results;
  let count = 0;
  for (let movieCount = 0;
       movieCount < theBody.count;
       movieCount++) {
    for (let characterCount = 0;
      characterCount < movieResults[movieCount].characters.length;
      characterCount++) {
      if (movieResults[movieCount].characters[characterCount] ===
        characterToFind) {
        count = count + 1;
      }
    }
  }
  console.log(count);
  if (error) {
    console.log(error);
  }
});
