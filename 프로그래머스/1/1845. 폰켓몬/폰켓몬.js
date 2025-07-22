function solution(nums) {
    var answer = new Set(nums)
    console.log(answer)
    
    const answerLen = answer.size;
    console.log(answer.answerLen);
    
    if (answerLen > nums.length/2){
        return nums.length/2
    }else{
        return answerLen
    }
    
    
    
    
    return answer;
}