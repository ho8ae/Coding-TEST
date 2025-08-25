function solution(word) {
    var answer = 0;
    let dic = []
    const vowels = ['A','E','I','O','U'];
    
    // dfs로 재귀로 탐색하면 되지 않을까?
    function dfs(currentWord){
        // lenth가 5면 재귀 종료
        if(currentWord.length === 5) return;
        
        for(let i=0; i<vowels.length; i++){
            let newWord = currentWord+vowels[i]
            dic.push(newWord);
            dfs(newWord);
        }
        
    }
    
    // 그냥 처음 부터 시작하고 만들자
    dfs("");
    
    // console.log(dic)
    return dic.indexOf(word)+1;
}