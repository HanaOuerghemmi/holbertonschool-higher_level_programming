#!/usr/bin/node
const fs = require('fs');
const { argv } = process;

const path = argv[2];

fs.readFile(path, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
}

);
