function solution(bridge_length, max_weight, wait_truck_weights) {
    let queue = []
    let time = 0
    let current_weight = 0
    
    while(queue.length>0 || wait_truck_weights.length>0){
        time++
        
        if(queue.length>0 && queue[0][1] === time){
            let end_truck = queue.shift()[0]
            current_weight -= end_truck
        }
        
        if(wait_truck_weights.length>0 && current_weight + wait_truck_weights[0] <= max_weight){
            let truck = wait_truck_weights.shift()
            queue.push([truck, time+bridge_length])
            current_weight += truck
        }
    }
    
    return time;
}