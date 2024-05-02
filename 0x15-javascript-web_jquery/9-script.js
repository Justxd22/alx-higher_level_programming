$('document').ready(function () {
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (value) { $('DIV#hello').text(value.hello); });
});
