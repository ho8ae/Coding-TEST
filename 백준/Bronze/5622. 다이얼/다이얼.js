const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim();

solution(input);

function solution(input) {
  let answer = 0;

  for (let i = 0; i < input.length; i++) {
    let temp = input.charCodeAt(i);

    if (temp >= 65 && temp <= 67) {
      answer += 3;
    } else if (temp >= 68 && temp <= 70) {
      answer += 4;
    } else if (temp >= 71 && temp <= 73) {
      answer += 5;
    } else if (temp >= 74 && temp <= 76) {
      answer += 6;
    } else if (temp >= 77 && temp <= 79) {
      answer += 7;
    } else if (temp >= 80 && temp <= 83) {
      answer += 8;
    } else if (temp >= 84 && temp <= 86) {
      answer += 9;
    } else if (temp >= 87 && temp <= 90) {
      answer += 10;
    }
  }

  console.log(answer);
}