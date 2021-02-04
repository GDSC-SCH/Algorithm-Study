//12-9 10814

const fs = require('fs');
//const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const input = ['3', '21 Junkyu', '21 Dohyun', '20 Sunyoung']; //입력 오류로 임시 할당으로 대체
const sortAge = new Array(201);

input.map(list => {
  const splited = list.split(' ');
  const num = parseInt(splited[0]);
  if (sortAge[num] === undefined) {
    sortAge[num] = [];
  }

  sortAge[num].push([num, splited[1]]);
});

let results = '';
sortAge.map(list => {
  if (list) {
    for (let i = 0; i < list.length; i++) {
      results += `${list[i][0]} ${list[i][1]}\n`;
    }
  }
});

console.log(results);
