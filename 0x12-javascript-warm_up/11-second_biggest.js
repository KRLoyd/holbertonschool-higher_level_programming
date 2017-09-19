#!/usr/bin/node
// Script to search for the second biggest integer in a list of arguments
let argListLen = process.argv.length;
if (argListLen <= 3) {
  console.log('0');
} else {
  let firstBiggest = parseInt(process.argv[2]);
  let secondBiggest = parseInt(process.argv[2]);
  for (let i = 3; i < argListLen; i++) {
    if (parseInt(process.argv[i]) > secondBiggest && parseInt(process.argv[i]) < firstBiggest) {
      secondBiggest = parseInt(process.argv[i]);
    } else if (parseInt(process.argv[i]) > firstBiggest) {
      secondBiggest = firstBiggest;
      firstBiggest = parseInt(process.argv[i]);
    }
  }
  console.log(secondBiggest);
}
