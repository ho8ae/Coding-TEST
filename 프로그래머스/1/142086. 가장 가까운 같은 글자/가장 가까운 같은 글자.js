function solution(s) {
    var answer = [];
    
    let dic = [];
    
    for (let c of s){
        if(!dic[c]){
            dic[c]=0
        }
    }
    
  
    for(let i = 0; i<s.length; i++){
        // 만약 아직 0이라면
        if(dic[s[i]] == 0){
            answer.push(-1)
            // 1 더하기
            dic[s[i]] += 1
        }
        
        // 0이 아니라면 i=3 부터
        else{
            let mn = 10000
            let temp;
            for(let j=0; j<i; j++){
                if(s[j] == s[i]){
                    temp = i-j
                }
                if(mn > temp){
                    mn = temp
                }
            }
            answer.push(mn)
        }
        
    }
      console.log(dic)
    console.log(answer)
    return answer;
}