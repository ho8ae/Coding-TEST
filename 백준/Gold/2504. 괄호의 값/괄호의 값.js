const input = require('fs').readFileSync('/dev/stdin').toString().trim();

function solution(bracket) {
    let stack = [];
    
    for (let char of bracket) {
        if (char === '(' || char === '[') {
            // 여는 괄호는 스택에 추가
            stack.push(char);
        } else if (char === ')' || char === ']') {
            // 닫는 괄호를 만났을 때
            let value = 0;
            
            while (stack.length > 0 && typeof stack[stack.length-1] === 'number') {
                // 숫자들을 더함
                value += stack.pop();
            }
            
            if (stack.length === 0) {
                // 스택이 비어있으면 잘못된 괄호
                return 0;
            }
            
            let openBracket = stack.pop();
            
            if ((char === ')' && openBracket !== '(') || (char === ']' && openBracket !== '[')) {
                // 괄호 쌍이 맞지 않으면 잘못된 괄호
                return 0;
            }
            
            // 값 계산
            if (value === 0) {
                value = (char === ')') ? 2 : 3;
            } else {
                value *= (char === ')') ? 2 : 3;
            }
            
            stack.push(value);
        } else {
            // 괄호가 아닌 다른 문자가 있으면 잘못된 입력
            return 0;
        }
    }
    
    // 최종 결과 계산
    let result = 0;
    for (let value of stack) {
        if (typeof value === 'number') {
            result += value;
        } else {
            // 숫자가 아닌 값(괄호)이 남아있으면 잘못된 괄호
            return 0;
        }
    }
    
    return result;
}

console.log(solution(input));