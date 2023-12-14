#!/usr/bin/node
function factorio (n) {
  if (isNaN(n)) {
    return (1);
  }
  if (n > 1) {
    return (n * factorio(n - 1));
  } else {
    return (1);
  }
}
console.log(factorio(process.argv[2]));
