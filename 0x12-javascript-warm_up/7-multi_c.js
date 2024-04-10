#!/usr/bin/node

const rep = Math.floor(Number(process.argv[2]));

for (let i = 0; i < rep; i++) {
  if (isNaN(rep)) {
    console.log('Missing number of occurrences');
    break;
  }
  console.log('C is fun');
}
