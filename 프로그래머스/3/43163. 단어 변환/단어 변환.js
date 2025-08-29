function solution(begin, target, words) {
    // target이 words에 없으면 return 0
    if(!words.includes(target)){
        return 0;
    }
    
    // 한 글자 만 다른지? 변환 체크
    const canTransform = (word1, word2) => {
        let diff = 0;
        for(let i =0; i<word1.length; i++){
            if(word1[i] !== word2[i]){
                diff++
            }
        }
        return diff === 1
    }
    
    // bfs 풀기
    const q = [[begin,0]] //시작,횟수
    const v = new Set() // 중복 x
    
    while(q.length > 0){
        // q 꺼내기
        const [currentWord, steps] = q.shift();
        
        // 종료 조건
        if(currentWord === target){
            return steps;
        }
        
        for(const word of words){
            // 방문 했거나, 변환 불가능하면 skip
            if(v.has(word) || !canTransform(currentWord,word)) continue;
            
            v.add(word);
            q.push([word,steps+1])
        }
        
    }
    
    return steps;
}