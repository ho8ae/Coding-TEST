const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]);
const numbers = input[1].split(' ').map(Number);
let count = 0;

function isPrime(n) {
    if (n < 2) return false;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) return false;
    }
    return true;
}

for (let i = 0; i < N; i++) {
    if (isPrime(numbers[i])) {
        count++;
    }
}

console.log(count);