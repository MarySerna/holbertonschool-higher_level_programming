#!/usr/bin/node
/*
Script that prints the first argument passed to it
*/
const numArg = process.argv[2];
if (numArg === undefined) {
  console.log('No argument');
} else {
  console.log(numArg);
}
