function solution(numbers) {
    let answer = '';
    
    let arr = numbers.map(String).sort((a,b) => (b+a) - (a+b))
    
    for(let x of arr){
        answer += x
    }
    
    if(answer.startsWith("0")) return "0"
    
    return answer;
}