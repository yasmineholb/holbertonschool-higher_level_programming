const ur = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(ur, function (mov) {
  for (var i = 0; i < mov.results.length; i++) {
    $('ul#list_movies').append(`<li>${mov.results[i].title}</li>`);
  }
});
