#!/usr/bin/node
const Rectangle = require('./3-rectangle').Rectangle;

const r1 = new Rectangle(2, 3);
r1.print();

const r2 = new Rectangle(10, 5);
r2.print();

// My test
const r3 = new Rectangle(undefined, undefined);
r3.print();

const r4 = new Rectangle( -9, 5);
r4.print()
