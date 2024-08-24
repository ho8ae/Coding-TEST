function solution(numbers) {
    const ret = [];
    // 두 수를 선택하는 모든 경우의 수를 반복문으로 구함
    for (let i =0; i<numbers.length; i++){
        for(let j = 0; j< i; j++){
            //두 수를 더한 결과를 새로운 배열에 추가
            ret.push(numbers[i] + numbers[j]);
        }
    }
    // 중복된 값을 제거하고, 오름차순으로 정렬 후 반환
    return [...new Set(ret)].sort((a, b) => a - b);
}