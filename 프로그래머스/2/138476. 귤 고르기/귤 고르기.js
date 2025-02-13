function solution(k, tangerine) {

    let hash = new Map()
    
    tangerine.forEach((item) => {
        hash.set(item, (hash.get(item) || 0)+1)
    })
    
    let arr = [...hash.values()].sort((a,b) => b-a)
    
    let count = 0
    let sum = 0
    
    for(let x of arr){
        sum += x
        count ++
        if(sum >= k) break
    }
    
    
    return count;
}