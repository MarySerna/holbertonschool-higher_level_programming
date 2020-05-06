#!/usr/bin/node
/*
Script that prints My number: <first argument converted in integer>
if the first argument can be converted to an integer
*/
const arg = process.argv[2];
const r = parseInt(arg);
if (isNaN(r)) {
  console.log('Not a number: ');
} else {
  console.log('My number ' + r);
}
