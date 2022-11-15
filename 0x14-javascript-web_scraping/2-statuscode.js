#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], (req, response) => {
  console.log(`code: ${response.statusCode}`);
});
