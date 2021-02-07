//15-1 11047
//var input = require('fs').readFileSync('/dev/stdin'); //임시 입력

var N = 10;
var K = 4200;
var output = 0;

const arr = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000];

while (N > 0) { //배열의 모든 수 조회
    if ( K >= arr[--N] ) { //인덱스임을 고려하여 N 활용
        output += parseInt(K/arr[N]); //특정 가치로의 최대 개수
        K = K % arr[N]; //나머지를 다음 연산에 활용하기 위함
    }
}

console.log(output);
