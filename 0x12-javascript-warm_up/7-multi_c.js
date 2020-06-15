#!/usr/bin/node
var m = process.argv[2];
if (typeof (process.argv[2]) === 'undefined') {
  console.log('Missing number of occurrences');
} else if (m < 0) {

}
for (var i = 1; i <= m; i++) {
  console.log('C is fun');
}
