function solution(board, moves) { 
    //[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    var answer = 0;
    
    // 0을 제외한 배열 재정의
    let arr = [];
    for(let i = 0; i<board.length; i++){
        arr.push([]);
        for(let j =0; j<board[i].length; j++){
           arr[i].push(board[j][i])
        }
    }
    
    // 체이닝도 마스터 함. V
    let arrFilter = arr.map(value => value.reverse().filter(v => v !== 0))
    // console.log(arrFilter)
    let basket = []
    
    for(let i =0; i<moves.length; i++){
        // 제일 위에꺼 크레인으로 뽑으니 pop()
        if(arrFilter[moves[i]-1].length >0){
        basket.push(arrFilter[moves[i]-1].pop());
        }
        // console.log("게임 배열",arrFilter);
        // console.log(`${i} 번째 현재 바구니 : ${basket}`)

        
        for(let j = 0; j<basket.length; j++){
            if(basket[j]===basket[j+1]){
                // console.log("똑같은 거 발견",basket[j]);
                basket.splice(j,2);
                // console.log("중복 삭제 후 바구니",basket)
                answer += 2;
            }
        }
    }
    
    
    
    return answer;
}