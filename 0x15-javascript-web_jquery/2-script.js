// Script to update the text color of HTML tag HEADER to red
// when tag DIV#red_header is clicked
const $ = window.$;
$('DIV#red_header').on('click', function () {
  $('HEADER').css('color', '#FF0000');
});
