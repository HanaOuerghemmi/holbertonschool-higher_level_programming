#!/usr/bin/node
const l = process.argv.length;
if (l <= 3) {
  console.log(0);
} else {
  const array = process.argv.map(Number)
    .slice(2, l).sort((a, b) => a - b);
  const len = array.length;
  console.log(array[len - 2]);
}
