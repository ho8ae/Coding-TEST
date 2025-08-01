const dx = [-1,1,0,0];
const dy = [0,0,-1,1];

function BFS(maps,v,a,b,dist){
    // console.log("BFS 시작")
    let n = maps.length;
    let m = maps[0].length;
    let q = [];
    q.push([a,b,dist]); // [x,y,distance];
    v[a][b] = true;
    // console.log("확인",q)
    
    while (q.length > 0){
        
        let [x,y,d] = q.shift();
        
        for(let i = 0; i<4; i++){
            let nx = x + dx[i];
            let ny = y + dy[i];
            
            if(0 <= nx && nx < n && 0 <= ny && ny < m && !v[nx][ny] && maps[nx][ny] !== 'X') {
            
                if(maps[nx][ny] === 'E'){
                    // console.log("d의 값",d)
                    return d+1;
                }
                
                v[nx][ny] = true;
                q.push([nx, ny, d + 1]); 
            }
        }
    }
    
    return -1

}

function findL(maps, v, a, b) {
    let n = maps.length;
    let m = maps[0].length;
    let q = [];
    q.push([a, b, 0]); // [x, y, distance]
    v[a][b] = true;
    
    while (q.length > 0) { 
        let [x, y, dist] = q.shift();
        
        for(let i = 0; i < 4; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];
            
            if(0 <= nx && nx < n && 0 <= ny && ny < m && !v[nx][ny] && maps[nx][ny] !== 'X') {
                if(maps[nx][ny] === 'L') {
                    
                    // v를 다시 초기화
                    let v = [];
                    for(let i = 0; i < n; i++) {
                        v.push([]);
                        for(let j = 0; j < m; j++) {
                            v[i].push(false);
                        }
                    }
                    return BFS(maps,v,nx,ny,dist + 1); 
                }
                v[nx][ny] = true;
                q.push([nx, ny, dist + 1]); 
            }
        }
    }
    
    
    return -1;
}

function solution(maps) {
    let n = maps.length;
    let m = maps[0].length;
    
    // 방문 그래프 초기화
    let v = [];
    for(let i = 0; i < n; i++) {
        v.push([]);
        for(let j = 0; j < m; j++) {
            v[i].push(false);
        }
    }
    
    // 시작점 찾기
    for(let i = 0; i < n; i++) {
        for(let j = 0; j < m; j++) {
            if(maps[i][j] === 'S') {
                let findLNumber = findL(maps, v, i, j);
                // console.log("레버까지의 거리:", findLNumber);
                
                if(findLNumber === -1) {
                    return -1;
                }
                
                return findLNumber;
            }
        }
    }
    
    // console.log(v)
    
    return -1;
}