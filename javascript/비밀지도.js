function solution(n, arr1, arr2) {
    var answer = [];
    let newboard = Array.from(Array(n), () => Array(n).fill(0))
    
    for (let i = 0; i < n; i++){
        let arr1_item = arr1[i].toString(2).split("").reverse();
        let arr2_item = arr2[i].toString(2).split("").reverse();
        
        for (let j = 0; j < arr1_item.length; j++){
            if (arr1_item[j] === "1"){
                newboard[i][j] = 1
            }
        }        
        for (let k = 0; k < arr2_item.length; k++){
            if (arr2_item[k] === "1"){
                newboard[i][k] = 1
            }
        }        
    }

    for (let i = 0; i < n; i++){
        var taew = newboard[i].reverse().map(e => e === 1 ? "#" : " ").join("");
        answer.push(taew);
    }

    return answer;
}

solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28])