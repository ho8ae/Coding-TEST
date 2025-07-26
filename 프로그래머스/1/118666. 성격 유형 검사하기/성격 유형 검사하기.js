// 각 성격 유형 검사 데이터
const 성격지표 = {R:0,T:0, C:0,F:0, J:0,M:0, A:0,N:0}
const 성격마지막 = {R:false,T:false, C:false,F:false, J:false,M:false, A:false,N:false}
const 성격 = ["R","T","C","F","J","M","A","N"];
const 점수표 = [0,3,2,1,0,1,2,3];
function solution(survey, choices) {
    var answer = '';
    
    // dic으로 저장해버림
    let currentData = {};
    
    // survey split으로 짜름
    for(let i = 0; i<survey.length; i++){
        let survey_split = survey[i].split('');
        // console.log("자른 데이터", survey_split) // 이 자른 데이터로 저장
        if(choices[i] == 1 || choices[i] == 2 || choices[i] == 3 ){
            
            // dic으로 접근
            if(!currentData[survey_split[0]]){
                currentData[survey_split[0]] = 점수표[choices[i]]
            }else{
                currentData[survey_split[0]] += 점수표[choices[i]]
            }
            
        }
        
        if(choices[i] == 5 || choices[i] == 6 || choices[i] == 7 ){
              // dic으로 접근
            if(!currentData[survey_split[1]]){
                currentData[survey_split[1]] = 점수표[choices[i]]
            }else{
                currentData[survey_split[1]] += 점수표[choices[i]]
            }
        }
    }
    
    console.log(survey, choices)
  
    console.log("dic 처리 끝난 현재 데이터", currentData)
    
    // 성격 지표 업데이트
    for(let i =0; i<Object.keys(currentData).length; i++){
     
        성격지표[Object.keys(currentData)[i]] += Object.values(currentData)[i]
    }
   
    console.log("성격지표 업데이트", 성격지표)
    
    let 성격배열 = []
    
    for(let i = 0; i<Object.keys(성격지표).length; i++){
        성격배열.push(Object.values(성격지표)[i]);
    }
    
    console.log(성격배열)
    
    // 2개씩순회하면서 큰 거 골라서 넣기 
    for(let i = 0; i<성격배열.length; i+=2){
        
            
        // 만약 같다면 ? 
        // if(성격배열[i] === 성격배열[i+1]){
        //     // 키를 통해 비교 뭐가 더 큰지
        //     if(Object.keys(성격마지막)[i] < Object.keys(성격마지막)[i+1]){
        //         성격마지막[i] = true;
        //         성격마지막[i+1]  = false;
        //         continue;
        //     }else{
        //         성격마지막[i+1] = true;
        //         성격마지막[i] = false;
        //         continue;
        //     }
        // }
            
        if(성격배열[i]>=성격배열[i+1]){
            성격마지막[i]=true;
        }else{
            성격마지막[i+1]=true;
        }
    }
    
    console.log("성격마지막",성격마지막)
    
    for(let i = 0; i<Object.keys(성격마지막).length; i++){
        if(Object.values(성격마지막)[i]==true){
            answer += 성격[Object.keys(성격마지막)[i]];
        }
    }
    
    console.log("답",answer)

    
    return answer;
}