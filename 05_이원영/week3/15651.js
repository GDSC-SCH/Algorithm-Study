//13-3 15651

const input = [3, 1];
const N = input.shift();
const M = input.shift();
const output = [];
let result = '';

function bt(cnt) {
  if (cnt === M) {
    result += `${output.join(' ')}\n`;
    return;
  }

  for (let i = 0; i < N; i++) {
    output.push(i + 1);
    bt(output.length);
    output.pop();
  }
}

bt(0);

console.log(result.trim());
