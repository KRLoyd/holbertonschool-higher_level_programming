// Script to add the class 'red' to HTML tag 'HEADER'
// when tag 'DIV#red_header' is clicked
const $ = window.$;
$('DIV#red_header').on('click', function () {
  $('HEADER').addClass('red');
});
