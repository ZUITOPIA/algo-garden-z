function solution(d, budget) {
    let count = 0;
    let sum = 0
    
    let arr = d.sort((a,b) => a-b)
    
    for(let i=0;i<d.length;i++){
        sum += arr[i]
        if(sum > budget) break
        count ++
    }
    
    return count;
}