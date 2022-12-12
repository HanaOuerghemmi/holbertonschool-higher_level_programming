#!/usr/bin/node

exports.esrever = function (list) {
  const l = [];
  for (let i = list.length - 1; i > -1; i--) {
    l.push(list[i]);
  }
  return l;
};
