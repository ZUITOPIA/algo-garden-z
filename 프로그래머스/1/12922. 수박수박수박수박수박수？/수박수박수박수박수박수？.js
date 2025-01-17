function solution(n) {
    let answer = ''
    let word = ["수", "박"]
 
    for(let i=0;i<n;i++){
        answer += word[i%2]
    }
    
    return answer;
}