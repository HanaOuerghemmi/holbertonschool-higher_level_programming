#!/usr/bin/node
const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    const size = this.height;
    for (let i = 0; i < size; i++) {
      console.log(c.repeat(size));
    }
  }
};
