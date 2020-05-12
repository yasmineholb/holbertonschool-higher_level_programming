#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const fl = process.argv[3];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(fl, body, 'utf-8', function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});
