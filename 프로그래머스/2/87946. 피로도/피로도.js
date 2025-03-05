function solution(k, dungeons) {
    let max_count = 0
    let visited = Array(dungeons.length).fill(false)
    
    function dfs(fatique, count){
        max_count = Math.max(max_count, count)
        
        for(let i=0; i<dungeons.length; i++){
            if(!visited[i] && fatique >= dungeons[i][0]){
                visited[i] = true
                dfs(fatique - dungeons[i][1], count+1)
                visited[i] = false
            }
        }
    }
    
    dfs(k, 0)
    
    return max_count;
}