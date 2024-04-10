#!/usr/bin/node

const size = Math.floor(Number(process.argv[2]));

for (let i = 0; i < size; i++) {
  if (isNaN(size)) {
    console.log('Missing size');
    break;
  }
  for (let j = 0; j < size; j++) {
    console.log('X');
  }
}
