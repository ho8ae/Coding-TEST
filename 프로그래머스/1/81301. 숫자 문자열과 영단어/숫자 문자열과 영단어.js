const numberDic = {
    zero:'0',
    one:1,
    two:2,
    three:3,
    four:4,
    five:5,
    six:6,
    seven:7,
    eight:8,
    nine:9
}
function solution(s) {
    // 문자열 계속해서 저장하다가 맞으면 새 배열에 Push
    let answer = []
    let tempString = ''
    for(let i =0; i<s.length; i++){
        tempString += s[i]
        console.log(tempString)
        if(/\d/.test(s[i])){
            answer.push(parseInt(s[i]))
            tempString = '' // 초기화
            continue;
        }
        if(numberDic[tempString] || numberDic[tempString] === '0'){
            answer.push(numberDic[tempString]);
            console.log(answer)
            tempString = '' // 초기화
            continue;
        }
     
    }

    answer = parseInt(answer.join(''))
    console.log("최종정답",answer)
    return answer;
}