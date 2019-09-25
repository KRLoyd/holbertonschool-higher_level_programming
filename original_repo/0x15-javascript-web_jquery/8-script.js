// Script to fetch and list all Star Wars movies `title`
// Titles will be listed in HTML tag 'UL#list_movies'
const $ = window.$;
const requestURL = 'https://swapi.co/api/films/?format=json';
$.get(requestURL, function (films) {
  let filmList = films.results;
  for (let movie = 0; movie < films.count; movie++) {
    $('UL#list_movies').append('<li>' + filmList[movie].title + '</li>');
  }
});
