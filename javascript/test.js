const fs = require('fs'); 
"use strict";
// 첫 줄 입력
const input = fs.readFileSync('javascript/test.txt').toString().split('\n'); 
const firstline = input[0].toString().split(' ').map(v => +v);

const N = firstline[0];
const K = firstline[1];

const board = [];

// 3차원 배열 초기화

var horseboard = new Array(3); 
for(var i=0; i< N; i++){
    horseboard[i] = new Array(N);
  for(var j=0; j<N; j++){
    horseboard[i][j] = new Array();
  }
}


const horsedir = {}

for (let i = 1; i <= N; i++){
    let num = input[i].split(' ').map(v => +v);    
    board.push(num);
}

let horseidx = 0
for (let k = N+1; k <= K+N; k++){
    let hs = input[k].split(' ').map(v => +v);
    const x = hs[0] - 1;
    const y = hs[1] - 1;           
        
    horseboard[x][y].push(horseidx);
    horsedir[horseidx] = hs[2] -1;

    horseidx++;
}

let result = 0;
// console.log(horsedir)
console.log(horseboard)


while (result < 1001){

    
    result++;
}

