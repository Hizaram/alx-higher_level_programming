#!/usr/bin/node
const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/:id';

if (process.argv.length > 2) {
  request(`${URL}/films/${process.argv[2]}/`, (err, res, body) => {
    if (err) {
      console.log(err);
    }
    console.log(JSON.parse(body).title);
  });
}
