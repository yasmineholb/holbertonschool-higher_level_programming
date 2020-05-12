#!/usr/bin/node

const fs = require('fs');
const request = require('request');
var url = process.argv[2];
var pr = request(url);
pr.pipe(fs.createWriteStream(process.argv[3]));
