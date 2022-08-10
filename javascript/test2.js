function solution(n){
    let answer = 0;      
    let counters = { 1: 4, 2:3, 3:1};

    const target = n.toString(2).replace(/0/g, "").length;

    if (n > 8)
    {
        let curr_val = 8;
        let curr_max = 4;
        while (curr_val * 2 < n){
            counters[curr_max] = 1;
            counters[curr_max-1] += 3;
            counters[curr_max-2] += 3;
            counters[1] += 1;

            curr_max++;
            curr_val *= 2;
        }
        
        answer += counters[target];        

        for (let i = curr_val; i < n; i++){
            if (target ===  i.toString(2).replace(/0/g, "").length){
                answer += 1;
            }
        }
    }
    else{
        for (let i = 0; i < n; i++){
            if (target ===  i.toString(2).replace(/0/g, "").length){
                answer +=1;
            }
        }
    }
    

    return answer;
}

solution(19);