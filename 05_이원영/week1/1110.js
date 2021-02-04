//4-3 1110
var input = 26;
var num = input;
var cycle = 0;

do {
    cycle++;
    var a = parseInt(num / 10);
    var b = num % 10;

    num = b * 10 + ((a+b) % 10);
} while(input != num)

console.log(cycle);
