// 입력
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let count = input[0];
let numbers = [];

for (let i = 1; i < input.length; i++) {
  if (input[i] !== '') {
    numbers.push(input[i].split(' '));
  }
}

for (let i = 0; i < numbers.length; i++){
  let num1 = Number(numbers[i][0]);
  let num2 = Number(numbers[i][1]);

  console.log(num1 + num2);
}


// Basic usage example
import Heap from 'heap-js';


// 2차원 배열 회전
arr = [[1,2,3], [4,5,6]]
const zip = (rows) =>rows[0].map((_,c)=> rows.map(row => row[c]));
zip([...arr])


// 요소 정렬
var cars = [
    { type: 'Volvo', year: 2016 },
    { type: 'Saab', year: 2001 },
    { type: 'BMW', year: 2010 },
];

var ret = cars.sort(function (a, b){
    return a.year - b.year;
})

// 스택 구현
const stack = [];

stack.push(1);
stack.push(2);
stack.push(3);

stack[stack.length - 1]; // peek 3
stack.pop(); // 3
stack.pop(); // 2
stack.pop(); // 1

// 큐 구현1
const queue = [];

queue.push(1); // enqueue 1
queue.push(2); // enqueue 2
queue.push(3); // enqueue 3

queue.shift(); // dequeue 1
queue.shift(); // dequeue 2
queue.shift(); // dequeue 3

// 큐 구현2
class node {
    constructor(val) {
        this.value = val;
        this.next = null;
    }

    setNext(n) {
        this.next = n;
    }
}

class Queue {
    constructor() {
        this.head = null;
        this.tail = null;
        this._size = 0;
    }

    push(node) {
        if (this.head == null) {
            this.head = node;
        } else {
            this.tail.next = node;
        }
        this._size++;
        this.tail = node;
    }

    pop() {
        if (this.head == null) return -1;

        let returnNode = this.head;
        if (this.head != this.tail) this.head = this.head.next;
        else {
            this.head = null;
            this.tail = null;
        }
        this._size--;
        return returnNode;
    }
    
    size() {
        return this._size;
    }
}

// 맵 규현, 시간복잡도 O(1)
const map = new Map();
map.set('p1', 1);
map.set('p2', 2);

map.get('p1'); // 1
map.get('p2'); // 2

// 집합
const set = new Set();
set.add(1);
set.add(2);

set.has(1); // true
set.has(2); // true
set.has(3); // false

// 2차원 배열 초기화
const arr1 = Array.from(Array(5), () => new Array(2))


// 3차원 배열 초기화

var horseboard = new Array(3); 
for(var i=0; i< N; i++){
    horseboard[i] = new Array(N);
  for(var j=0; j<N; j++){
    horseboard[i][j] = new Array();
  }
}

function getPermutations(array, size) {

    function p(t, i) {
        if (t.length === size) {
            result.push(t);
            return;
        }
        if (i + 1 > array.length) {
            return;
        }
        p(t.concat(array[i]), i + 1);
        p(t, i + 1);
    }

    var result = [];
    p([], 0);
    return result;
}

var array = ['a', 'b', 'c', 'd'];


const binarySearch = (list, target, left, right) => {
    let mid = 0;
  
    while (left <= right) {
      // 가운데 인덱스
      mid = Math.floor((left + right) / 2);
  
      if (list[mid] === target) {
        return mid;
      }
      
      // 대소 비교로 범위 지정
      if (list[mid] > target) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }
  
    return -1;
  }

console.log(getPermutations(array, 2));