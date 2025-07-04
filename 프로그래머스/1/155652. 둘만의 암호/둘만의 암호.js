function getNextChar(char){
    if(char === 'z'){
        return 'a';
    }
    return String.fromCharCode(char.charCodeAt(0) + 1);
}

function solution(s, skip, index) {
    const skipSet = new Set(skip)
    let result = '';
    console.log(skipSet)
    
    for(const char of s){
        let currentChar = char;
        let steps = 0;
        
        while(steps < index){
            currentChar = getNextChar(currentChar);
           if(!skipSet.has(currentChar)){
               steps++;
           }
        }
        
        result += currentChar;
    }
    
    
    
    return result;
}