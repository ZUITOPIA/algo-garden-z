function solution(n, words) {
    
    let record = new Set()
    record.add(words[0])
    
    for(let i=1; i<words.length; i++){
        let prev = words[i-1]
        let curr = words[i]
        
        if(record.has(curr) || prev[prev.length-1] !== curr[0]){
            let order = i%n+1
            let round = Math.floor(i/n)+1
            return [order, round]
        }
        
        record.add(curr)
    }
    
    
    return [0, 0];
}