//15-5 11399
//var input = require('fs').readFileSync('/dev/stdin'); //임시 입력 처리

const N = 5;
var arr = [3, 1, 4, 3, 2];
var time = 0;

arr.sort(); //각 시간은 가중되기 때문에 그리디 알고리즘을 바탕으로 가장 작은 수부터 우선 배치

var add = 0;
for (var i = 0; i<N;i++) { //마지막 사람이 기다리는 총 시간
    add += arr[i];
    time += add;
}

console.log(time);
