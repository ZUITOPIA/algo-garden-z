function solution(sizes) {
    let width = 0
    let height = 0
    
    for(let [x,y] of sizes){
        let min = Math.min(x,y)
        let max = Math.max(x,y)
        
        width = Math.max(min, width)
        height = Math.max(max, height)
    }
    
    return width*height;
}