function solution(keymap, targets) {
    let answer = [];
    
    let indexArr = {};
    
    keymap.forEach(item => {
        [...item].forEach((char, index) => {
            let itemIdx = index+1;
            
            if(indexArr[char] === undefined){
                indexArr[char] = itemIdx;
            } else {
                indexArr[char] = Math.min(itemIdx, indexArr[char]);
            }

        });
    });
    
    targets.forEach(item => {
        let sum = 0;
        let isExist = true;
        
        [...item].forEach(char => {
            if(indexArr[char] === undefined){
                isExist = false;
            } else {
                sum += indexArr[char];
            }
        })
    
        if(isExist){
            answer.push(sum);          
        } else {
            answer.push(-1);
        }
    });
    
    return answer;
}