function solution(n, wires) {
    
    let answer_min = Infinity
    
    function dfs(node, visited, graph){
        visited[node] = true
        let count = 1
        
        for(let next of graph[node]){
            if(!visited[next]){
                count += dfs(next, visited, graph)
            }
        } return count
    }
    
    
    for(let [a,b] of wires){
        let graph = Array.from({length: n+1}, ()=>[])
        
        for(let [x, y] of wires){
            if((x===a && y===b) || (x===b && y===a)) continue
            
            graph[x].push(y)
            graph[y].push(x)
            
        }
        
        
        let visited = Array(n+1).fill(false)
        let s_1 = dfs(1, visited, graph)
        let s_2 = n - s_1
        
        answer_min = Math.min(answer_min, Math.abs(s_1-s_2))
        
        
    }
    return answer_min
}