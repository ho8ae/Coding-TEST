function findWeakNumber(num){
    let result = [];
    for(let i =1; i<=num/2; i++){
        if(num%i === 0) result.push(i);
    }
    return result.length;
}

function solution(number, limit, power) {
    var answer = 0;
    let arr = [];

    for(let i=1; i<number+1; i++){
        arr.push(findWeakNumber(i)+1);
    }
    
    for(let i=0; i<arr.length; i++){
        if(arr[i]>limit) answer+=power;
        if (arr[i]<=limit) answer+=arr[i];
        
    }
    return answer;
}