function solution(arr, divisor) {
    
    let tempArr = arr.sort((a,b)=>a-b)
    
    let answer = tempArr.filter(item => item % divisor === 0)
    
    if(answer.length<=0) return [-1]
    
    return answer;
}