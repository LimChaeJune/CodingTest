function solution(msg) {
    var answer = [];
    
    const alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
            
    for (let i = 0; i < msg.length; i++){
        let skip = 0;    
        if (i < msg.length-1){
            for (let j = i+2; j <= msg.length + 2; j++){            
                if (alpha.includes(msg.substring(i,j))){                
                    skip++;                 
                    if (j === msg.length + 2){
                        const idx = alpha.indexOf(msg.substring(i,j));
                        answer.push(idx+1);
                        i += skip;
                    }
                }
                else{
                    const value = msg.substring(i,j)
                    const idx = alpha.indexOf(msg.substring(i,j-1));
                    answer.push(idx+1);
                    alpha.push(value);
                    i += skip;
                    break;
                }
            } 
        }
        else{
            const idx = alpha.indexOf(msg.substring(i));
            answer.push(idx+1);
        }
           
    }
    
    return answer;
}

solution("TOBEORNOTTOBEORTOBEORNOT");