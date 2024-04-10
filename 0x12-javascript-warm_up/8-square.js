#!/usr/bin/node

const size = Math.floor(Number(process.argv[2]));

let row = '';

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let j = 0; j < size; j++) {
    row += 'X';
  }

  for (let i = 0; i < size; i++) {
    console.log(row);
  }
}
