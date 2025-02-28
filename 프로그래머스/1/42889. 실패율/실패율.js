function solution(N, stages) {
    let stages_length = stages.length
    
    let arr = []    
    let map = new Map()
    
    stages.forEach((i) => map.set(i, (map.get(i) || 0 ) + 1))

    
    for(let i=1; i<=N; i++){
        let fail = map.get(i) ? map.get(i) / stages_length : 0
        
        stages_length -= map.get(i) || 0
    
        arr.push([i, fail])
    }
    
    arr.sort((a,b) => b[1] - a[1])
    
    
        
    
    return arr.map(([stage]) => stage)
}