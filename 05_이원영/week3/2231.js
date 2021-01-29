//11-2 2231
var N = 216; //입력 오류로 임시 할당
var M, m;

for (var i = 1 ; i < N ; i++) {
    M = i;
    m = i;
    
    while (m) {
        M += m % 10;
        m = parseInt(m/10);
    }

    if (M == N) {
        console.log(i);
        break;
    }
}
