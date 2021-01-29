//11-3 7568
var n = 5;
var arr = [[55, 185], [58, 183], [88,186], [60, 175], [46, 155]];
var out = [];

for (var i = 0; i < n; i++) {
    var bigger = 1;
    
    for (var j = 0; j<n ; j++) {
        if (i !== j && arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1] ) {
            bigger++;
        }
    }

    out[i] = bigger;
}

for (var i = 0; i< n ; i++) {
    console.log(out.join(' '));
}
