// Script to update the text of HTML tag 'HEADER'
// When 'DIV#update_header' is clicked
const $ = window.$;
$('DIV#update_header').on('click', function () {
  $('HEADER').text('New Header!!!');
});
