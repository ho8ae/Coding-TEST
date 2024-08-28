function isVaildMove(nx,ny){
    //좌표평면 벗어났는지 쳌
    return nx >= -5 && nx<=5 && ny>=-5 &&ny<=5;
}

function updateLocation(x,y,dir){
    switch(dir){
        case "U":
            return [x,y+1];
        case "D":
            return [x,y-1];
        case "R":
            return [x+1,y];
        case "L":
            return [x-1,y];
            
    }
}

function solution(dirs) {
    let x =0;
    let y=0;
    
    const visited = new Set(); //겹치는 좌표는 1개로 처리하기 위함
    for(const dir of dirs){
        const [nx,ny] = updateLocation(x,y,dir)
        
        if (!isVaildMove(nx,ny)){
            continue;
        }
        
    visited.add(`${x}${y}${nx}${ny}`);
    visited.add(`${nx}${ny}${x}${y}`);
    
    [x,y] = [nx,ny];
    
    }
    return visited.size/2
}