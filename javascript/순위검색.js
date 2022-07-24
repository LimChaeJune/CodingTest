let fs = require('fs');
let input = fs.readFileSync('javascript/test.txt').toString();

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]);


function solution(info, query) {    
    let answer = [];
    let comb = {}
    
    function combination(score, comb, item, start){
        const key = item.join("");        

        if (comb[key]){
            comb[key].push(score);            
        }
        else{
            comb[key] = [score];           
        }
        for (let i = start; i < item.length; i++){
            let item_slice = item.slice();
            item_slice[i] = "-";
            combination(score, comb, item_slice, i + 1);                
        }
    }    
        

    function binary_search(map, key, score) {
        let scoreArr = map[key];

        if (scoreArr) {
            let start = 0;
            let end = scoreArr.length;
            while (start < end) {
                let mid = Math.floor((start + end) / 2);

                if (scoreArr[mid] >= score) { //현재 가르키는 값보다 내가 찾는 값이 
                    end = mid;
                } else if (scoreArr[mid] < score) {
                    start = mid + 1;
                }
            }
            return scoreArr.length - start;
        }
        else return 0
    }

    for (i of info){
        const item = i.split(" ");
        const score = Number(item.pop()); 
        combination(score,comb,item, 0);
    }

    for (let key in comb){
        comb[key].sort((a,b) => a - b);
    }

    for (q of query){
        const query_item = q.replace(/ and /g, "").split(" ");
        const score = Number(query_item.pop());
        answer.push(binary_search(comb, query_item.join(""), score));
    }
        
    
    return answer;
}