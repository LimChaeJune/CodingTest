function solution(p) {
    function isCorrect(w){
        let left = 0;
        let right = 0;
        for (let i = 0; i < w.length; i++){
            if (w[i] === '('){
                left++;
            }
            else{
                right++;
                if (right > left){
                    return false;
                }
            }            
        }
        return true;
    }    

    if (p === ''){
        return '';
    }

    if (isCorrect(p)){
        return p;
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