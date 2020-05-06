#!/usr/bin/node
/*
Script that prints My number: <first argument converted in integer>
if the first argument can be converted to an intege
*/
const tyArg = process.argv[2];
if (isNaN(tyArg)) {
  console.log('Not a number');
} else {
  console.log('My number is: ' + tyArg);
}
