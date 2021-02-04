//2-5 2884
var H = 10;
var M = 10;

if (H - 45 < 0) {
    M = 60 - (45 - M);
    H -= 1;
    if (H < 0) {
        H =23;
    }
    console.log(H+' '+M); 
}

else console.log(H+' '+(M-45)); 
