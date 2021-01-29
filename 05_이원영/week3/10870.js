//10-2 10870
//const fs = require("fs");
//const input = fs.readFileSync("/dev/stdin");
//const n = parseInt(input);
const n = 10; //입력 오류로 임시 할당

const fibonacci = (n, a, b) => {
    if (n === 0) {
        return a;
    }
    return fibonacci(n-1, b, a+b);
};

if ( n === 0 || n === 1) {
    return console.log(n);
}

const result = fibonacci(n, 0, 1);
console.log(result);
