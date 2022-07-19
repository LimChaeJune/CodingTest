function solution(A, B) {    
    if (A.length === 1){
        return 1;
    }
    else if (A.length === 0){
        return 0;
    }
    
    let result = 1;
    let end = B[0];
    for (let i = 1; i < A.length; i++){
        if (end < A[i]){
            result += 1;
            end = B[i];
        }
    }

    return result;
}

solution([1,3,7,9,9],[5,6,8,9,10]);
