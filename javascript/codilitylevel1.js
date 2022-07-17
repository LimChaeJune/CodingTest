
solution(15)

function solution(N) {    
    const binaryNum = N.toString(2);

    const idx = binaryNum.slice(binaryNum.indexOf('1'), binaryNum.lastIndexOf('1'));

    const result = idx.split("1").map(zero => zero.length);

    return result ? Math.max(...result) : 0;
}