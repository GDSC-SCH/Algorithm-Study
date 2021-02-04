//2-3 2753
var year = 2000;

if (year%4==0 && year% 100!=0) console.log('1');
else if (year%100==0 && year%400!=0) console.log('0');
else if (year%400==0) console.log('1');
else  console.log('0');
