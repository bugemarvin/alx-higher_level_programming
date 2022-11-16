#!/usr/bin/node
const request = require('request');
request.get(`https://swapi-api.hbtn.io/api/people/${process.argv[2]}`, (err, req, res) => {
  if (err) throw err;
  const chars = 'https://swapi-api.hbtn.io/api/people/'.filter(process.argv[2]);
  for (let i = 0; i <= chars; i++) {
    console.log(i);
  }
});
