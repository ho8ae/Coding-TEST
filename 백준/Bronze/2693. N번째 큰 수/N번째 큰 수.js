const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const T = Number(input[0]);

function findThirdLargest(line) {
    const numbers = line.split(' ').map(Number);
    numbers.sort((a, b) => b - a);
    return numbers[2];
}

for (let i = 1; i <= T; i++) {
    const result = findThirdLargest(input[i]);
    console.log(result);
}