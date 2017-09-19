#!/usr/bin/node
let argLen = 0;
for (; process.argv[argLen]; argLen++) {

}
if (argLen === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
