function solution(clothes) {
    let hash = new Map()
    
    for(let c of clothes){
        let type = c[1]
        hash.set(type, (hash.get(type) || 0)+1)
    }
    
    let result = 1
    for(let count of hash.values()){
        result *= (count+1)
    }
    
    return result-1
}