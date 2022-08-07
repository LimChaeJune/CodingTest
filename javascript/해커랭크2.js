
function extraLongFactorials(n) {
    n = BigInt(n)
    let result = BigInt(1);
    
    
    for(let i = n; i >= 1; i--) {
      result *= i;
    }
    
    console.log(result.toString());
    return result.toString();
}

extraLongFactorials(5);