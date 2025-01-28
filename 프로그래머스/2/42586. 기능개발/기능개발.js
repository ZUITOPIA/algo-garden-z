function solution(progresses, speeds) {
    
    let days = progresses.map((item, i) => Math.ceil((100-item)/speeds[i]))
    
    let max = days[0]
    let result = []
    let count = 0
    
    for(let x of days){
        if(x <= max){
            count ++
        } else {
            result.push(count)
            count = 1
            max = x
        }
    }
    result.push(count)
    
    return result
}