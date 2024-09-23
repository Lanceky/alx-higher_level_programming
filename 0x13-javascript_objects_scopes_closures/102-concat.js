#!/usr/bin/node
const fs = require('fs');

const [,, fileA, fileB, fileC] = process.argv;

fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) {
      console.error(err);
      return;
    }
    fs.writeFile(fileC, dataA + dataB, (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
});

