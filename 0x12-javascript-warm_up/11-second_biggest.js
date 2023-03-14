#!/usr/bin/node
const list = process.argv;
if (list[3]) {
  list.sort(function (a, b) { return b - a; });
  console.log(list[3]);
} else console.log(0);
