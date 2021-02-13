//17-5 1874
const fs = require('fs');
//const input = fs.readFileSync('/dev/stdin').toString().split('\n'); //임시 할당

var num = 8;   //임시 할당
var arr = [4, 3, 6, 8, 7, 5, 2, 1];
var stack = [];

var max = 0;   //0보다 큰 정수들만 있기 때문에
for (var i = 0; i < num; i++) {
    if ( arr[i] > max ) {
        for (var j = max; j < arr[i]; j++) {
            stack.push(j);
            console.log('+');
        }
    }

    else if (stack.top != arr[i]) {
        console.log("NO");
        return;
    }

    stack.pop;
    console.log('-');
    if (arr[i] > max) max = arr[i]
}
