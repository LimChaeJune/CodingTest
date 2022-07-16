let fs = require('fs');
let input = fs.readFileSync('javascript/test.txt').toString();

solution(input);

function solution(new_id){    
    const isAlpha = /^[a-z|A-Z]+$/;    
    const isNumber = /^[0-9]+$/;

    const lower_id = new_id.toLowerCase();

    let newStr = ""
    for (ch of lower_id){
        if (isAlpha.test(ch) || isNumber.test(ch)){
            newStr += ch;
        }
        else if (ch === "-" || ch === "_" || ch === ".")
        {
            newStr += ch;
        }
    }
    
    // .. 연속 제거
    while (newStr.includes("..")){
        newStr = newStr.replace('..','.');
    }

    
    // 처음 끝 제거
    if (newStr[0] === "."){
        newStr = newStr.substring(1);
    }
    if (newStr.slice(-1) === '.'){
        newStr = newStr.substring(0, newStr.length - 1);
    }
    

    // 빈 문자열이라면
    if (newStr == "")
    {
        newStr = "a";
    }   
    else if (newStr.length > 15){
        newStr = newStr.slice(0, 15);
        if (newStr.slice(-1) === "."){
            newStr = newStr.slice(0, 14);
        }
    }

    if (newStr.length < 3){
        for (i = newStr.length; i < 3; i++){
            newStr += newStr.slice(-1);
        }
    }
    

    return newStr;
}
