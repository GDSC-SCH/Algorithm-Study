//9-3 11653
var num = 72;

var i = 2;
while(true) {
    if (num % i == 0) {
        console.log(i);
        num = num/i;
    }

    else i++;

    if (num == 1) break;
}
