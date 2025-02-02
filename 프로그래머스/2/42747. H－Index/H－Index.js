function solution(citations) {
    let answer = 0
    
    let sorted_citations = citations.sort((a,b) => b-a) 
    
    for(let i=0; i<sorted_citations.length; i++){
        let h = i+1
        if(sorted_citations[i] >= h) answer=h
        else break
    }
    
    return answer;
}