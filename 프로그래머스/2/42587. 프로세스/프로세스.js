function solution(priorities, location) {
    let answer = 0
    let queue = priorities.map((priority, i) => [priority, i])
    
    while(queue.length){
        let temp = queue.shift()
        
        if(queue.some((item) => item[0] > temp[0])){
            queue.push(temp)
        } else {
            answer++
            if(temp[1] === location) return answer
        }
    }
}