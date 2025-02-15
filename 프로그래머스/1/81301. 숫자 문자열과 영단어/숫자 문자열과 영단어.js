function solution(s) {
    let arr = new Map([["0","zero"], ["1","one"], ["2","two"], ["3","three"], ["4","four"], ["5","five"], ["6","six"], ["7","seven"], ["8","eight"], ["9","nine"]])
    
    for(let [num, str] of arr){
        s = s.split(str).join(num)
    }
    
    return Number(s)
}