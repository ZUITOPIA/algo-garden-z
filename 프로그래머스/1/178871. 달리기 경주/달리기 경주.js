function solution(players, callings) {
    
    let rank = Object.fromEntries(players.map((item, index) => [item,index]))
    
    for(let c of callings){
        let current = rank[c]
        
        if(current > 0){
            prev = players[current-1]
            players[current-1] = c
            players[current] = prev
            
            rank[c] -= 1
            rank[prev] += 1 
            
        }   
    }
    return players;
}