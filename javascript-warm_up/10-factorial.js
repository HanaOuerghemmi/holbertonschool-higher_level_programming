#!/usr/bin/node

function factorial (x) {
  if (isNaN(x)) {
    return 1;
  } else if (x === 0) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}

const x = parseInt(process.argv[2]);
console.log(factorial(x));
