const dx = [-1,1,0,0]
const dy = [0,0,-1,1]

// function BFS(place,i,j){
//     let q = []
//     q.push([i,j])
//     place[i][j] = 'X'; // 일단 방문을 X 처리
//     const result = true;
    
//     while (q){
//         x,y = q.shift()
//     }
    
// }


function find(place,a,b){
    
    // 상하좌우에 P가 있으면 return false;
    
    
    for(let i=0; i<4; i++){
        // 범위 넘어가면 continue
        x= a+dx[i];
        y= b+dy[i];
        
        console.log("x,y",x,y)
        
        if(x<0 || x>=5 || y<0 || y>=5){
            continue;
        }
        
        if(place[x][y] === 'P'){
            console.log("바로 옆에 P가 있는 경우")
            return false;
        }
        
        if(place[x][y] === 'O'){
            console.log("주위에 O가 있는 경우")
            tx = x;
            ty = y;
            
            for(let j = 0; j<4; j++){
                nx = tx+dx[j];
                ny = ty+dy[j];
                if(nx<0 || nx>=5 || ny<0 || ny>=5 || (nx === a && ny === b)){
                    continue;
                }
                
                if(place[nx][ny] === 'P'){
                    
                    console.log("O 주위에 P가 옆에 있어요 !",nx,ny)
                    return false;
                }
            }
        }
    }
    
    return true;
    
    
    // 상하좌우에 O가 있으면 그 자리로 이동 후 P가 있으면 return false 단, 처음 위치 빼고 거기는 X로 바꿔
    
}

const findRule = (place) => { // 'POOPX', 'OXPXP', 'PXXXO', 'OXXXO', 'OOOPP' 
    console.log("place",place)
    
    // 우선 첫 P를 찾기
    for(let i = 0; i<place[0].length; i++){
        for(let j =0; j<place.length; j++){
            if(place[i][j] === 'P'){
                result = find(place,i,j);
                if(!result){
                    return 0;
                }
            }
        }
    }
    
    return 1;
}

function solution(places) {
    var answer = [];
    
    // places 별로 순회
    for(let place of places){  
        console.log("=========새로운 Place 시작 ! ============")
     answer.push(findRule(place));
    }
    
    console.log("답", answer)
    
    return answer;
}


