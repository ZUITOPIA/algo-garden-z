function solution(brown, yellow) {    
    let sum = brown+yellow
    
    for(let height=1; height<=Math.sqrt(sum); height++){
        if(sum%height === 0){
            let width = sum / height
            
            if((width-2)*(height-2) === yellow) return [width, height]
        }       
    }
    
}