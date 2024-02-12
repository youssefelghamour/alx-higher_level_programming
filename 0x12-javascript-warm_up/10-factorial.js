#!/usr/bin/node

let x = parseInt(process.argv[2]);
if (!x) {
  console.log(1);
} else {
  let f = 1;
  while (x > 0) {
    f *= x;
    x--;
  }
  console.log(f);
}
