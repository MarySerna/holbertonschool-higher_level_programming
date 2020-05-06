#!/usr/bin/node
/*
Write a script that searches the second biggest integer in the list of arguments
*/
let nextMax = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  args.sort(function (a, b) {
    return a - b;
  });
  nextMax = args[args.length - 2];
}
console.log(nextMax);
