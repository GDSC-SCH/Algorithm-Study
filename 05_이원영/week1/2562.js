//5-2 2562
var arr = [3, 29, 38, 12, 57, 74, 40, 85, 61]; //입력 관련 미해결점 다른 언어로 해결

var max = arr[0];
var maxIndex = 0;

for (var i = 1; i<9;i++) {
    if (max < arr[i]) {
        max = arr[i];
        maxIndex = i+1;
    }
}

console.log(max);
console.log(maxIndex);
