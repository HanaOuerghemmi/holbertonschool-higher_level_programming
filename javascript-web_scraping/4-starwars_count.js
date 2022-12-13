#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) throw error;
  const films = JSON.parse(body).results;
  const wedgeFilms = films.filter(film => film.characters.some(characters =>
    characters.includes('/18')));
  console.log(wedgeFilms.length);
});
