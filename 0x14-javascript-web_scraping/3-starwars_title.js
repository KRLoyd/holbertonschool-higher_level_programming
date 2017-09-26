#!/usr/bin/node
// Script to print the title of a Star Wars movie
// Movie episode number matches the passed integer
const request = require('request');
const episodeNumber = process.argv[2];
let requestURL = 'http://swapi.co/api/films/' + episodeNumber;

request(requestURL, function (error, response, body) {
  let theBody = JSON.parse(body);
  console.log(theBody['title']);
  if (error) {
    console.log(error);
  }
});
