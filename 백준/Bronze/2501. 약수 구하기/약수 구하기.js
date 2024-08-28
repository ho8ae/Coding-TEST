const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');
const N = parseInt(input[0]);
const K = parseInt(input[1]);

function findKthDivisor(N, K) {
    let count = 0;
    for (let i = 1; i <= N; i++) {
        if (N % i === 0) {
            count++;
            if (count === K) {
                return i;
            }
        }
    }
    return 0;  // K번째 약수가 없는 경우
}

const result = findKthDivisor(N, K);
console.log(result);