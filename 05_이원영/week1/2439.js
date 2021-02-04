// 3-10 2439
var num = 5;

for (var i = 1; i <= num ; i++) {
    for (var j = 0; j< 5-i; j++) {
        console.log('');
    }

    for (var j = 0; j < i;j++) {
         console.log('*');
    }
    
    console.log('\n');
}
