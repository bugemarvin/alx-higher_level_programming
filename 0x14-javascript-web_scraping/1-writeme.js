#!/usr/bin/node
const fs = require('fs');
const info = process.argv[3];
fs.writeFile(process.argv[2], info, (err) => {
  console.error(err);
});
