// create a new list
// with the value 1,2,3,4
// (ignores the input)
// returns:
//   [1,2,3,4]
function reset(x) {
  let r = [];
  for (let i = 1; i <= 4; i++) {
    r.push(i);
  }

  return r;
}

console.log(JSON.stringify(reset([1, 1, 2, 3, 3, 4, 1, 2, 7, 9])));
