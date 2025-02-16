function solution(n) {
    let n_one = n.toString(2).split("1").length-1
    
    while(true){
        n++
        if(n.toString(2).split("1").length-1 === n_one) return n
    }
   
}