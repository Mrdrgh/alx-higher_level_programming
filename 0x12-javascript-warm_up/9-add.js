#!/usr/bin/node
function add(a, b) {
  return (a + b);
}
if (process.argv[2] === undefined || process.argv[3] === undefined
    || isNaN(process.argv[2]) || isNaN(process.argv[3])) {
  console.log('invalid args');
} else {
  console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
}
