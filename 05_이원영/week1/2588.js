//1-11 2588
var x = 472;
var y = 385;

var a = x * ((y%100)%10);
var b = x * ((y%100)/10);
var c = x * (y/100);
var d = x * y;

console.log(a);
console.log(b);
console.log(c);
console.log(d);
