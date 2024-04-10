#!/usr/bin/node

const size = Math.floor(Number(process.argv[2]));

let row = ''

for (let j = 0; j < size; j++) {
  row += 'X'
}

for (let i = 0; i < size; i++) {
  if (isNaN(size)) {
    console.log('Missing size');
    break;
  } else {
    console.log(row)
  }
}
