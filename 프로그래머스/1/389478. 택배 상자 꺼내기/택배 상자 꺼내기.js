function solution(n, w, num) { // 22, 6, 8 ,  reuslt = 3
    var answer = 0;
    let arr = [];
    let flag = 1
    
    // 배열 만들기 n/w + 1 은 
    for(let i=0; i<(n/w); i++){
        arr.push([])
    }
    console.log(arr)
    
    let idx = 0
    
    for(let i =0; i<arr.length; i++){
        for(let j = 0; j<w; j++){
            if(flag > n){
                arr[i].push(0);
                flag +=1
                continue
            }
            arr[i].push(flag);
            flag +=1
        }
        // 홀수면
        if(i % 2 !== 0){
            arr[i].reverse();
        }
    }
    
    console.log(arr)
    
    // x 열 y 행
    let x,y = 0
    
    // 순회하면서 밑에있는거 찾기
    for(let i=0; i<arr.length; i++){
        for(let j =0; j<arr[i].length; j++){
            if(arr[i][j]===num){
                x=j
                y=i
                break;
            }
        }
    }
    console.log(x,y)
    
    for(let i = y; i<arr.length; i++){
        if(arr[i][x] > 0){                
            answer += 1;
        }
    }
    console.log(answer)

    
    return answer;
}