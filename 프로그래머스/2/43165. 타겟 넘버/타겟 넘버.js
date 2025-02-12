function solution(numbers, target) {
    let count = 0;
    
    function DFS(index, sum){
        if(index === numbers.length){
             if(sum === target){
                count += 1
             }
            return
        }
        DFS(index+1, sum + numbers[index])
        DFS(index+1, sum - numbers[index])
    }
    
    DFS(0,0)
    
    return count;
}