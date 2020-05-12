#!/usr/bin/node

const lss = require('./100-data').list;
console.log(lss);
console.log(lss.map((x, nm) => x * nm));
