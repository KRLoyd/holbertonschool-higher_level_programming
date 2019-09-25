// Script to add a `LI` element to `UL.my_list`upon click of tag `DIV#add_item`
const $ = window.$;
$('DIV#add_item').on('click', function () {
  $('UL.my_list').append('<li>Item</li>');
});
