#!/usr/bin/node

exports.esrever = function (list) {
  const m = [];
  for (let i = list.length - 1; i >= 0; i--) {
    m.push(list[i]);
  }
  return m;
};
