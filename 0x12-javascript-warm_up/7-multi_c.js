#!/usr/bin/node
/*  prints 3 lines: (like 1-multi_languages.js) but by using an array
of string and a loop
*/

const x = process.argv[2];

if (x === undefined || isNaN(parseInt(x))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(x); i++) {
    console.log('C is fun');
  }
}
