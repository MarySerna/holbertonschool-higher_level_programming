#!/usr/bin/node
/*
Script that prints a message depending of the number of arguments passed
*/
const numArg = process.argv.length;
if (numArg === 2) {
  console.log('No argument');
} else if (numArg === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
