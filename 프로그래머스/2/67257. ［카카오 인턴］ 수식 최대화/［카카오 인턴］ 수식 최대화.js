/**
숫자들과 3가지의 연산문자(+ ,- ,*) 우선순위를 자유롭게 재정의하여 큰 숫자를 제출
같은 순위의 연산자는 없어야 한다.
음수여도 됨. -> 절대값으로 숫자가 가장 큰 참가자로 우승
*/


function solution(expression) {
    var answer = 0;
    
    // 숫자,연산자 분리
    const numbers = expression.split(/[\+\-\*]/).map(Number);
    const operators = expression.match(/[\+\-\*]/g);
    console.log(`numbers ${numbers}`)
    console.log(`operators ${operators}`)
    const operatorSet = [...new Set(operators)];
    console.log(operatorSet) // <- 이미 배열
    
    // 우선 순위 만들기 이거를 만들어서 하나씩 돌려보기
    let priorities = [];
    
    // dfs로 우선순위 판단
    function makePermutation(arr,selected){
        // 모든 타입 들어가면 push
        if(selected.length === arr.length){
            priorities.push([...selected]);
        }
        
        for(let i =0; i<arr.length; i++){
            if(selected.includes(arr[i])) continue;
            selected.push(arr[i]);
            makePermutation(arr,selected);
            selected.pop();
        }
    }
    
    makePermutation(operatorSet,[]);
    
    console.log(priorities);
    
    
    
    // 계산 함수
    function calculate(nums,ops,priority){
        // 원본 복사
        let numArr = [];
        let opArr = [];
        for(let n of nums) numArr.push(n);
        for(let o of ops) opArr.push(o);
        
        // 우선 순위 높은 대로 계산
        for(let op of priority){
            // 해당 연산자를 찾아서 계산
            for(let i = 0; i<opArr.length; i++){
                if(opArr[i] === op){
                    let result;
                    
                    // 연산 수행
                    if(op === "+"){
                        result = numArr[i] + numArr[i+1];
                    } else if (op === "-"){
                        result = numArr[i] - numArr[i+1];
                    }else if (op === "*"){
                        result = numArr[i] * numArr[i+1];
                    }
                    
                    //배열 계산 , 배열 가공 ( 계산 했으니 )
                    numArr.splice(i,2,result)
                    opArr.splice(i,1);
                    i--; // 인덱스 조정
                }
            }
        }
        // 절대값으로 return
        return Math.abs(numArr[0])
        
    }
    
    
    // 만들어진 우선순위로 계산해서 최댓값 찾기
    let maxValue = 0;
    
    for(let priority of priorities){
        let value = calculate(numbers,operators,priority);
        if (value > maxValue){
            maxValue = value;
        }
    }
    
    return maxValue;
    
    
    
    
    
    
    return answer;
}