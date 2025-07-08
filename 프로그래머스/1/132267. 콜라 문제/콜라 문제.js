function solution(a, b, n) {
    var answer = 0;
    while (n >= a){
        let tmp_coke = Math.floor(n/a);
        console.log("tmp_coke",tmp_coke)
        let tmp_bottle = n%a 
        console.log("tmp_bottle",tmp_bottle)
        answer += tmp_coke*b
        console.log("answer",answer)
        n = tmp_bottle + (tmp_coke * b)
        console.log("n",n)
    }
    return answer;
}
