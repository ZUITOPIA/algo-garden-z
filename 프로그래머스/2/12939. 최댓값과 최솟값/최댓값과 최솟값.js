function solution(s) {
    var answer = '';
    
    let arr = s.split(" ").map((item) => Number(item)).sort((a,b) => a-b)
    
    return arr[0] + " " + arr[arr.length-1]
}