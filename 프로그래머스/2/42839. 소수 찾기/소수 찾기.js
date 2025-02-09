function getPermutation(arr){
    let result = new Set()
    
    function dfs(prefix, remaining){
        if(prefix.length !== 0) result.add(Number(prefix))
        
        for(let i=0; i<remaining.length; i++){
            let new_arr = [...remaining]
            new_arr.splice(i,1)
            
            dfs(prefix + remaining[i], new_arr)
        }
    }
    
    dfs("", arr)
    return result
}

function isPrime(n){
    if(n < 2) return false
    
    for(let i=2; i<= Math.sqrt(n); i++){
        if(n%i===0) return false
    }
    return true
}

function solution(numbers) {
    let arr = numbers.split("")
    let perm = getPermutation(arr)
    let count = [...perm].filter(isPrime).length
    return count
}