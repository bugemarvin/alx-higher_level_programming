#!/usr/bin/node

const request = require('request');
request.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (err, req, res) => {
  if (err) console.error(err);
  const info = JSON.parse(res).characters;
  for (const userName of info) {
    request(userName, (err, req, res1) => {
      if (err) console.error(err);
      console.log(JSON.parse(res1).name);
    });
  }
});
