#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
<<<<<<< HEAD
const url = 'https://swapi-api.hbtn.io/api/films/' + id + '/';
=======
const url = 'http://swapi.co/api/films/' + id;
>>>>>>> parent of cd2bd42... verif

request.get(url, function (error, resp, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
