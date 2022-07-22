class LRU {
    constructor(max = 30) {
        this.max = max;
        this.cache = new Map();
    }

    get(key) {
        let item = this.cache.get(key);
        if (item) {
            // 키 위치 변경
            this.cache.delete(key);
            this.cache.set(key, item);
        }
        return item;
    }

    set(key, val) {
        if (this.max > 0){
            // 키 위치 변경
            if (this.cache.has(key)) this.cache.delete(key);
            // 사이즈 초과시 첫번째 요소 삭제
            else if (this.cache.size == this.max) this.cache.delete(this.first());
            this.cache.set(key, val);
        }
    }    

    first() {
        return this.cache.keys().next().value;
    }
}



function solution(cacheSize, cities) {
    var answer = 0;
    const cache = new LRU(cacheSize, cities);
    for (city of cities){
       const value = cache.get(city.toLowerCase());

       if (value === undefined){
        answer += 5;
        cache.set(city.toLowerCase(), city.toLowerCase());
       }
       else{
        answer += 1;
       }
    }    
    return answer;
}

console.log(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])); 