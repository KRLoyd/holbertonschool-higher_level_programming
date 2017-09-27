#!/usr/bin/node
// Script to print the number of times character "Wedge Antilles" is present
const request = require('request');
const characterToFind = '18';
let requestURL = process.argv[2];

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let theBody = JSON.parse(body);
    let movieList = theBody.results;
    let count = 0;
    for (let movie in movieList) {
      let characterList = movieList[movie].characters;
      for (let character in characterList) {
        if (characterList[character].includes(characterToFind)) {
          count = count + 1;
        }
      }
    }
    console.log(count);
  }
});
