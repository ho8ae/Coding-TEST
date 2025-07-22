function solution(food) { // 1 3 4 6
    var answer = '';

    // 홀수가 되면 나머지는 버린다.
    let arr = [];
    
    // 우선 순회를 돌면서 배열 정리
    for(let i =1; i<food.length; i++){
        // 짝수가 아니면 -1
        if(food[i] % 2 !== 0 ){
            food[i] -= 1
        }
    }
    
    console.log(food)
    for(let i=1; i<food.length; i++){
        for(let j=0; j<food[i]/2; j++){
            answer += i
        }
    }
 
    answer += 0
    console.log(answer);
    
    for(let i=food.length; i>0; i--){
        for(let j=0; j<food[i]/2; j++){
            answer += i
        }
    }
    
    console.log(answer)
    
    
    
    return answer;
}