#!/usr/bin/node

const fs = require('fs');

const d = process.argv[3];

fs.writeFile(process.argv[2], d, 'utf-8', (err) => {
  if (err) throw err;
});
