#!/usr/bin/node

const request = require('request');
const id = '/18/';
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  let nb = 0;
  for (const film of JSON.parse(body).results) {
    for (const ch of film.characters) {
      if (ch.includes(id)) {
        nb += 1;
      }
    }
  }
  console.log(nb);
});
