#!/usr/bin/node
const fs = require('fs');
const info = process.argv[3];
fs.writeFile(process.argv[2], info, 'utf-8', (err) => {
  console.error(err);
});
