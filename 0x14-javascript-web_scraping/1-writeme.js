#!/usr/bin/node
const fs = require('fs');
let info = process.argv[3];
fs.writeFile(process.argv[2], info, (err) => {
  console.error(err);
});
