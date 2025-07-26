function solution(n) {
    var answer = 2;
    
    // 반복문 을통해서 min을 찾는건가? 그래서 나머지가 1이 되는 거 차는거지    
    while(true){
        if ( n%answer === 1 ) break;
        answer += 1
    }
    
    return answer;
}