#!/usr/bin/node
/*
Write a script that prints a square
*/
const x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
