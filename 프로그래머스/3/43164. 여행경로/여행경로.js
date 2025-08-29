function solution(tickets) {
    var answer = [];
    
    // 항공권을 dic으로 정리
    const graph = {};
    
    for(const [from,to] of tickets){
        if(!graph[from]){
            graph[from] = [];
        }
        graph[from].push(to);
    }
    
    // graph 가공
    for(const key in graph){
        graph[key].sort()
    }
    
    console.log("가공된 graph:",graph)
    
    // 방문 체크
    const v = Array(tickets.length).fill(false);
    
    function dfs(current,path){
         console.log(`현재: ${current}, 경로: ${path}, 길이: ${path.length}`);
    
    if(path.length === tickets.length + 1) {
        console.log("성공! 최종 경로:", path);
        answer = [...path];
        return true;
    }
        
        // grpah에서 해당하는 목적지 없으면 false
        if(!graph[current]) return false;
        
        for(let i=0; i<tickets.length; i++){
            const [from,to] = tickets[i];
            
            // 이미 방문 한 곳이거나, 현재 위치에서 출발 안하면 x
            if(v[i] || from !== current) continue;
            
            // 백트레킹 패턴
            v[i] = true;
            path.push(to);
            
            // 모든 항공권 사용되면 종료 될 때까지 dfs
            if(dfs(to,path)) return true;
            
            v[i] = false;
            path.pop(); // to 넣었던거 pop()
        }
        
        return false
    }
    tickets.sort();
    // 시작은 ICN 고정
    dfs("ICN",["ICN"]);
    

    return answer;
}