#!/usr/bin/node
/*
Script that prints My number: <first argument converted in integer>
if the first argument can be converted to an intege
*/
const arg = process.argv[2];
const r = parseInt(arg);
if (isNaN(r)) {
  console.log('Not a number');
} else {
  console.log('My number is: ' + r);
}
