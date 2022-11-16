#!/usr/bin/node
const request = require('request');
request.get(`${process.argv[2]}`, (err, req, res) => {
	if (err)  throw err;
	console.log(JSON.parse(res).name);
});
