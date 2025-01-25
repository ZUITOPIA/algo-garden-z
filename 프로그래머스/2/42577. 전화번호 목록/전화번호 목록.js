function solution(phone_book) {
    let hash = new Map()
    
    for(let phone of phone_book){
        hash.set(phone, true)
    }
    
    for(let phone of phone_book){
        let pre = ""
        for(let number of phone){
            pre += number
            if(pre != phone && hash.has(pre)) return false
        }
    }
    
    
    
    return true;
}