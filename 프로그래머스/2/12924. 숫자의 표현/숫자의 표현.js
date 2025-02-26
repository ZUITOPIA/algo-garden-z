function solution(n) {
    let count = 0;
 
    for (let start = 1; start <= n / 2; start++) {
        let sum = 0;


        for (let end = start; end <= n; end++) {
            sum += end;

            if (sum === n) {
                count++;
                break; 
            } else if (sum > n) {
                break;  
            }
        }
    }
    
    
    return count + 1;
}
