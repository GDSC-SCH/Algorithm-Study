//7-5 1157
var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString();

var numbers = input.split("\n")[1].split(" ");

var result = numbers.reduce((p, c) => {
    c = Number(c);
    p[0] > c ? p[0] = c : p[0] = p[0];
    p[1] < c ? p[1] = c : p[1] = p[1];
    return p
}, [1000000, -1000000]);

console.log(result.join(' '));
