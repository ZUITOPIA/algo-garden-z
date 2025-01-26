function solution(s) {
    let change_count = 0
    let zero_count = 0
    
    while(s !== "1"){
        let temp = ""
        for(let item of s){
            if(item === "0"){
                zero_count++
            } else {
                temp += item
            }
        }
        s = temp.length.toString(2)
        change_count++
    }
    
    return [change_count, zero_count];
}