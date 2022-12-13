#!/usr/bin/node
const request = require('request');
const { argv } = process;

const url = argv[2];

request(url, (error, response, body) => {
  if (error) throw error;
  console.log('code:', response.statusCode);
});
