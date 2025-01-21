function solution(arr) {

    let size = Math.max(arr.length, arr[0].length)
    
    for(let i=0; i<arr.length;i++){
        while(arr[i].length < size){
            arr[i].push(0)
        }
    }
    
    while(arr.length < size){
        arr.push(new Array(size).fill(0))
    }
    
 
    return arr;
}