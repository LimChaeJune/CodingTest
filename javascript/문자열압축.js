let fs = require('fs');
let input = fs.readFileSync('javascript/test.txt').toString();

solution(input);

"use strict";
function solution(s) {
    
    let answer = s.length;
    const maxsplit = Math.floor(s.length / 2);


    for (i = 1; i <= maxsplit; i++){
        let value = "";

        let count = 0;
        let prev = "";
        for (j = 0; j <= s.length; j += i) {
            if (prev === s.slice(j, j + i)) {
                count += 1;
            }
            else {
                if (count > 1){
                    value += count.toString() + prev;
                }
                else{
                    value += prev;
                }
                count = 1;
                prev = s.slice(j, j + i);
            }
        }         
        value += s.slice(j-i);

        answer = Math.min(answer, value.length);
    }

    console.log(answer);

    return answer;
}