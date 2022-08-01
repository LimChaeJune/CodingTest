function solution(dartResult) {
    var answer = 0;
    let values = []
    
    let temp = 0;
    for (let i = 0; i < dartResult.length; i++){
       if (!isNaN(dartResult[i])){
           if (dartResult[i] == 1 && dartResult[i+1] == 0){
               temp = 10;
               i++;
           }
           else{
               temp = dartResult[i];
           }
       }
       else if(dartResult[i] === 'S'){
           values.push(temp ** 1);
       }
        else if(dartResult[i] === 'D'){
           values.push(temp ** 2);
       }
        else if(dartResult[i] === 'T'){
           values.push(temp ** 3);
       }
        else if(dartResult[i] === '#'){
            values[values.length-1] *= -1;            
        }
        else if(dartResult[i] === '*'){
            values[values.length-1] *= 2;            
            values[values.length-2] *= 2;            
        }
    }
    
    for (let j = 0; j < values.length; j++){
        answer += values[j];
    }
    
    return answer;
}