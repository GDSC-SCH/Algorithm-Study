//5-7 4344
var num = 1; //입력 오류
var arr1 = [5, 50, 50, 70, 80, 100];
var pass = 0;

for (var i = 0; i < num; i++) {
    var size = arr1[0];
    var avg = 0;
    for (var j = 1; j<= size;j++ ) {
        avg += arr1[j];
    }
    avg /= size;

    for (var j = 1; j<= size;j++ ) {
        if (arr1[j] > avg) pass += 1;
    }
}

pass = pass/5*100
console.log(pass.toFixed(3));
