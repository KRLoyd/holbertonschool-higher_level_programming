// Script to toggle the class of HTML tag 'HEADER'
// when tag 'DIV#toggle_header' is clicked
// Toggles between classes 'red' and 'green'
const $ = window.$;
$('DIV#toggle_header').on('click', function () {
  if ($('HEADER').hasClass('red')) {
    $('HEADER').removeClass('red');
    $('HEADER').addClass('green');
  } else {
    $('HEADER').removeClass('green');
    $('HEADER').addClass('red');
  }
});
