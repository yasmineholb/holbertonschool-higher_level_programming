#!/usr/bin/node
if (process.argv[2] == null) {
  console.log('undefined is undefined');
} else if (process.argv.length === 3) {
  console.log(process.argv[2] + ' is undefined');
} else if (process.argv.length === 4) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
