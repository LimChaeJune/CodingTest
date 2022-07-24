function solution(p) {

    var answer = '';
    
    if (p === ""){
        return answer;
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

    let balance = 0;
    for (let i =0; i < p.length; i++){
        balance = p[i] === '(' ? balance +1 : balance -1;

        if (balance === 0){
            let u = p.slice(0, i+1);
            let v = p.slice(i+1);

            if (isCorrect(u)){
                v = solution(v);                                
                return u + v;
            }
            else{                
                let newV = '(' + solution(v) + ')';                
                for (let i = 1; i < u.length-1; i++){
                    newV = u[i] === '(' ? newV + ')' : newV + '(';
                }                               
                return newV;
            }

        }
    }
 
}

solution('()))((()');
