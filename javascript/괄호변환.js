function solution(p) {
    var answer = '';
    
    if (p === ""){
        return answer;
    }

    function isBalance(w){        
        let u = '';
        let v = '';
        // 균형잡힌 괄호 
        let result = 0;
        for (let i =0; i < w.length; i++){
            result = w[i] === '(' ? result + 1 : result - 1 ;
            if (result === 0){
                u = w.slice(0,i);
                v = w.slice(i);
            }
        }
        
    }

    function isCorrect(w){                
        const cnt =  0;
        for (let i =0; i < w.length; i++){            
            if (w[i] == '('){
                cnt += 1;
            }
            else{
                if (cnt == 0){
                    return false;
                }
                else{
                    cnt -= 1;
                }
            }                        
        }    

        return true;    
    }   

    if (isCorrect(p)){
        return p;
    }
    else{
        isBalance(p);
    }

    return answer;
}