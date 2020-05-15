const $ = window.$;
// $('header').addClass('red');
$('#toggle_header').click(function () {
  $('header').toggleClass('red');
  $('header').toggleClass('green');
});
