function solution(n){        
    let answer = -1;

    
    let target = 0;    

    let nLen = 1;    
    let nCnt = 9;

    while (n > nCnt * nLen){
        n -= (nLen * nCnt);
        target += nCnt;
        nLen++;
        nCnt *= 10;
    }

    target = Math.floor((target+1) + (n-1)/nLen);
    target_idx = (n-1)%nLen;
    answer = Number(target.toString().charAt(target_idx));        

    return answer;
}

console.log(solution(15));