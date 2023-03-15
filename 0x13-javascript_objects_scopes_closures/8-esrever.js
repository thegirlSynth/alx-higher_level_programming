#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (newList, element) {
    newList.push(element);
    return newList;
  }, []);
};
