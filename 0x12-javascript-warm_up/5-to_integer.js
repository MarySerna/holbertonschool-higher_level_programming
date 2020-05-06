#!/usr/bin/node
/*
Script that prints My number: <first argument converted in integer>
if the first argument can be converted to an intege
*/
let arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log('My number is: ' + arg);
}
