#!/usr/bin/node
list = require('./100-data').list;
newList = list.map((num) => num * list.indexOf(num));
console.log(list);
console.log(newList);
