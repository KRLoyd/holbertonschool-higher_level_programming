// Script to fetch 'name' from URL 'http://swapi.co/api/prople/5/?format=json'
// 'name' is then displayed in HTML tag 'DIV#character'
const $ = window.$;
const requestURL = 'https://swapi.co/api/people/5/?format=json';
$.get(requestURL, function (data) {
  $('DIV#character').text(data.name);
});
