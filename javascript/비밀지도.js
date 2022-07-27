function solution(n, arr1, arr2) {
    var answer = [];
    let newboard = []
    for (let i = 0; i < n; i++){
        let hec = arr1[i].toString(2).split("");
        for (let j = 0; j < hec.length; j++){
            console.log(hec[j]);
        }
    }
    
    return answer;
}

solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28])