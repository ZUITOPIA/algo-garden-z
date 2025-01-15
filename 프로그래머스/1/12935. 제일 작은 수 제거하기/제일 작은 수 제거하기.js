function solution(arr) {
    
    if(arr.length <= 1) return [-1]
    
    let mini = Math.min(...arr)
    
    arr.splice(arr.indexOf(mini), 1)
    
    return arr;
}