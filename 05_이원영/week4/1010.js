//16-9 1010
//var input = require('fs').readFileSync('/dev/stdin'); //임시 입력

const time = 3
var num = [[2, 2], [1, 5], [13, 29]];
var n;
var m;
var arr = [[],[]];

for (var i = 0; i <= m; i++) {
 arr[1][i] = i;
}

for (var t = 0; t < time; t++) {
    n = num[t][0];
    m = num[t][1];

    for (var i = 2; i <= n; i++) //엇갈리면 안되기 때문에 우측의 지점 선택의 경우의 수, 즉 조합만 고려하면 됨
    for (var j = i; j <= m; j++)
        for (var k = j; k >= i; k--) {
            arr[i][j] += arr[i - 1][k - 1];
        }

    console.log(arr[n][m]);
}
