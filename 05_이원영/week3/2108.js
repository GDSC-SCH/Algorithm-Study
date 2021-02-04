//12-4 2108

const input = [5, 1, 3, 8, -2, 2];
const N = input.shift();

var avg = 0;
for (let num of input) {
  avg += input[num];
}
avg /= 5;

const center = input[Math.floor(input.length / 2)];

const sortedNumArr = input.sort((a, b) => a - b);
const numMap = {};

for (let num of sortedNumArr) {
  if (numMap[num]) {
    numMap[num] = numMap[num] + 1;
  } else {
    numMap[num] = 1;
  }
}

var freNum = Math.max.apply(null, Object.values(numMap));
var freNumArr = [];
var freNumResult = 0;
for (let numKey in numMap) {
  if (numMap[numKey] === freNum) {
    freNumArr.push(numKey);
  }
}

if (freNumArr.length > 1) {
  freNumArr = freNumArr.sort((a, b) => a - b);
  freNumResult = freNumArr[1];
} else {
  freNumResult = freNumArr[0];
}

const area = sortedNumArr[sortedNumArr.length - 1] - sortedNumArr[0];

console.log(avg);
console.log(center);
console.log(freNumResult);
console.log(area);
