//골든 문제 9663

//var fs = require('fs');
//var read = fs.readFileSync('/dev/stdin').toString();
//var input = parseInt(input);
var input = 8;     //임시 할당
var output = 0;
var arr;

function checkBool(col) {
    for(var i = 0; i < col ; i++) {
        if (arr[i] == arr[col]) { return false; } //같은 열이면
		else if((arr[i] - arr[col]) == (col - i)) { return false; } //오른쪽아래 대각선방향이면
		else if((arr[col] - arr[i]) == (col-i)) { return false; }
    }

    return true;
}

function nQueen(row) {      //재귀반복
    if( row == input ) {
        output++;
    }

    else {
        for (var i = 0; i < input ; i++) {
            arr[row] = i;
            if(checkBool(row)) {
                nQueen(row+1);
            }
        }
    }
}

arr = new Array(input);
nQueen(0);
console.log(output);
