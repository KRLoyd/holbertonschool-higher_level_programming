#!/usr/bin/node
// Script to print all characters of a Star Wars movie
// Movie episode number matches the passed integer
const request = require('request');
const episodeNumber = process.argv[2];
let requestURL = 'http://swapi.co/api/films/' + episodeNumber;

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let characterList = JSON.parse(body).characters;
    for (let characterURL in characterList) {
      request(characterList[characterURL],
              function (error, response, body) {
                if (error) {
                  console.log(error);
                } else {
                  let name = JSON.parse(body).name;
                  console.log(name);
                }
              });
    }
  }
});
