function popcount(n){
    let count = 0;
    while(n>0n){
        count += Number(n & 1n); // 마지막 비트 수를 check
        n = n >> 1n;
    }
    return count;
}

function solution(k){ 
    let answer = popcount(k-1n) % 2;
    console.log(answer);
}

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let input;
rl.on("line", function(line){
    input = BigInt(line);
    // input = parseInt(line); // 입력 값이 정수라면 parseInt로 형변환
    rl.close();
}).on("close", function(){
    solution(input);
    process.exit();
})
