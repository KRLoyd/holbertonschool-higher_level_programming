#!/usr/bin/node
console.log(add(process.argv[2], process.argv[3]));
function add (a, b) {
  let c = parseInt(a) + parseInt(b);
  return c;
}
