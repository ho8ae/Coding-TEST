const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let dwarfs = input.map(Number);

function findSevenDwarfs(dwarfs) {
    for (let i = 0; i < 8; i++) {
        for (let j = i + 1; j < 9; j++) {
            // i번째와 j번째 난쟁이를 제외한 나머지 7명의 키 합 계산
            let sum = 0;
            let sevenDwarfs = [];
            
            for (let k = 0; k < 9; k++) {
                if (k !== i && k !== j) {
                    sum += dwarfs[k];
                    sevenDwarfs.push(dwarfs[k]);
                }
            }
            
            // 7명의 키 합이 100이면 결과 반환
            if (sum === 100) {
                return sevenDwarfs.sort((a, b) => a - b);
            }
        }
    }
}

let result = findSevenDwarfs(dwarfs);
console.log(result.join('\n'));