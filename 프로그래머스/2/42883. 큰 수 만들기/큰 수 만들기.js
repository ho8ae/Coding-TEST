function solution(number, k) {
    var answer = '';
    let stack = [];
    
    // 일단 순회하면서 stack에서 처리
    for(let i = 0; i<number.length; i++){    
        // 무한루프돌면서 작으면 다 처내기
        while(k>0 && stack[stack.length-1] < number[i]){
            stack.pop();
            k -= 1 ;     
        }
        stack.push(number[i]);
    }
    
    stack.splice(stack.length-1,k);
    console.log(stack)
    
    return stack.join("");
}