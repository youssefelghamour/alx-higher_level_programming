#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurence = 0;
  for (const num of list) {
    if (num === searchElement) {
      occurence++;
    }
  }
  return occurence;
};
