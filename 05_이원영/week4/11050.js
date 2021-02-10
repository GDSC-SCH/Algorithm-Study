//16-7 11050
//var input = require('fs').readFileSync('/dev/stdin'); //임시 입력

const N = 5;
const K = 2;
var arr = new Array(100);

for (var i = 0; i <= N; i++) {
    for (var j = 0; j <= Math.min(K,i); j++) {
        if (i == j || j == 0)
            arr[i, j] = 1;
        else
            arr[i, j] = arr[i - 1, j - 1] + arr[i - 1, j];
    }
}

console.log(arr[N, K]);
