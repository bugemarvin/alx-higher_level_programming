#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], (err, req, res) => {
  if (err) throw err;
  const info = JSON.parse(res).results;
  let i = 0; let values = 0;
  for (const key in info) {
    for (values of info[key].characters) {
      if (values.includes('18')) i++;
    }
  }
  console.log(i);
});
