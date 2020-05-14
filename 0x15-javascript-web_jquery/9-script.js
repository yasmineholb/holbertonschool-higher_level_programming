const ur = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.getJSON(ur, function (val) {
  $('div#hello').text(val.hello);
});
