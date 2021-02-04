//5-4 3052
var num = [1,2,3,4,5,6,7,8,10]  //입력 오류
var arr = [];

for (var i = 0; i<10;i++) {
    if(arr.indexOf(num[i]) === -1) {
        arr.push(num[i]);
    }
}

console.log(arr.length);
