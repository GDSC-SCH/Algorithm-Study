//14-8 1463

//var input = require('fs').readFileSync('/dev/stdin').toString();

const num = 2; //입력 오류로 임시할당

const arr = new Array(num + 1).fill(0);

for (let i = 2; i <= num; i++) {
  arr[i] = arr[i - 1] + 1;

    if (i % 2 === 0) {
      arr[i] = Math.min(arr[i], arr[i / 2] + 1);
    }

    if (i % 3 === 0) {
      arr[i] = Math.min(arr[i], arr[i / 3] + 1);	
    }
}

console.log(arr[num]);
