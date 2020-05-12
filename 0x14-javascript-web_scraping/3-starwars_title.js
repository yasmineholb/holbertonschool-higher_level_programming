#!/usr/bin/node

const rq = require('request');
const id = process.argv[2];
const url = 'http://swapi.co/api/films/' + id;

rq.get(url, function (error, resp, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
