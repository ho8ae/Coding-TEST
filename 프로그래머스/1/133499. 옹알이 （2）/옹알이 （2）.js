function solution(babbling) {
    var answer = 0;
    
    const words = ["aya", "ye", "woo", "ma"];
    for(let i = 0; i < babbling.length; i++){
        let temp = '';
        let lastWord = ''; 
        
        for(let j = 0; j < babbling[i].length; j++){
            temp += babbling[i][j];
            
            // 단어 체크
            if(words.includes(temp)){
                
                // 단어 중복 체크
                if(lastWord === temp){
                    babbling[i] = "fail";
                    break;
                }
                
                // 마지막 단어 저장
                lastWord = temp;
                
                // babbling[i]를 가공하고, j and temp 초기화
                babbling[i] = babbling[i].substring(temp.length);
                j = -1;
                temp = '';
            }
        }
        
        if(babbling[i].length === 0){
            answer += 1;
        }
    }
    
    return answer;
}