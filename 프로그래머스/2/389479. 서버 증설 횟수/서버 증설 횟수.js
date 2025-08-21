function solution(players, m, k) {
    var answer = 0;
    let currentServer = []
   
    // 각 시간마다 순회하며 따라 게임 이용자 수로 판단
    for(let i =0; i< players.length; i++){
        
        // 만료된 서버 체크
        currentServer = currentServer.filter(time => time>i);
        
        // 현재 인덱스의 게임 이용자 수
        let player = players[i]
        console.log(`현재 이용자 수 :${player}`);
        
        // 이용자 수 m 미만이면 skip
        if(player < m) continue;
        
        // 할당 가능한 서버인지 체크
    
        
        let needServerCount= parseInt(player/m);
        console.log(`현재 ${i}시 입니다. 서버를 확인합니다. 필요 서버 ${needServerCount}`)
        let currentServerCount = currentServer.length;
        
        // 추가로 필요한 서버 수
        let additionalServers = needServerCount - currentServerCount

        // 서버가 있다면 조건 패스
        if(additionalServers > 0){
            console.log(`현재 시간${i}, ${additionalServers}대 서버 증설 필요`);
            
            for(let j = 0 ; j<additionalServers; j++){
                currentServer.push(i+k);
                answer += 1
            }
            
        }
        
        
    }
    
    
    return answer;
}
