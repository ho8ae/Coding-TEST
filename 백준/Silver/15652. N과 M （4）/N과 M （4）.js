const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let N, M;
const rs = [];

function recur(num, start) {
    if (num === M) {
        console.log(rs.join(' '));
        return;
    }
    
    for (let i = start; i <= N; i++) {
        rs.push(i);
        recur(num + 1, i);
        rs.pop();
    }
}

rl.on('line', function(line) {
    [N, M] = line.split(' ').map(Number);
    recur(0, 1);
    rl.close();
});