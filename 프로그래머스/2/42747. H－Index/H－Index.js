function solution(citations) {
    let answer = 0
    
    citations.sort((a,b) => b-a) 
    
    for(let i=0; i<citations.length; i++){
        let h = i+1
        if(citations[i] >= h) answer=h
        else break
    }
    
    return answer;
}