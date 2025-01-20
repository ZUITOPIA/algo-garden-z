function solution(s) {
    var answer = '';
    
    let arr = s.split(" ")
    
    return Math.min(...arr) + " " + Math.max(...arr)
}