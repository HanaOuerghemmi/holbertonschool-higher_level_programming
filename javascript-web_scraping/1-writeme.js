#!/usr/bin/node
const fs = require('fs');
const { argv } = process;

const path = argv[2];
const data = argv[3];

fs.writeFile(path, data, 'utf8', err => {
    if (err) {
        console.error(err);
        return;
    }
}

);
