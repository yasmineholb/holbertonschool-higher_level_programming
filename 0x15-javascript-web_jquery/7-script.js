const $ = window.$;
const ur = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(ur, function (na) {
  $('div#character').text(na.name);
});
