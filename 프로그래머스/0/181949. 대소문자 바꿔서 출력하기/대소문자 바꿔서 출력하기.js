const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();

let str = input // 입력 값 받기
let result = ''; 

// 각각 해야하니까 split , for문 반복은? 빠르게
str.split('').forEach((value,index)=> {
    if (value == value.toUpperCase()){
        result += value.toLowerCase();
    }else{
        result += value.toUpperCase()
    }
});
console.log(result)