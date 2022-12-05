#!/usr/bin/node
const str = 'C is fun';
let i = 0;
const n = parseInt(process.argv[2]);
if (n) {
  while (i < n) {
    console.log(str);
    i++;
  }
} else {
  console.log('Missing number of occurrences')
}
