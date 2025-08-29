function solution(n, computers) {
    var answer = 0;
    
    // visited arr 정의
    let v = Array(n).fill(false);
    
    // 노드 개수 만큼 반복
    for(let i=0; i<n; i++){
        if(!v[i]){
            answer++;
            dfs(i);
        }
    }
    
    function dfs(index){
        // 방문 완료
        v[index] = true;
        
        const computer = computers[index];
        
        for(let i=0; i<computer.length; i++){
            const isConnect = computer[i] === 1 ? true : false;
            if(!v[i] && isConnect){
                dfs(i)
            }
        }
        
    }
    
    
    return answer;
}