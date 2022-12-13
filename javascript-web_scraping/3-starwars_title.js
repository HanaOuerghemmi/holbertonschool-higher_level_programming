#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://swapi-api.hbtn.io/api/films';
const { argv } = process;

const id = argv[2];

request(`${apiUrl}/${id}`, (error, response, body) => {
  if (error) throw error;
  console.log(JSON.parse(body).title);
});
